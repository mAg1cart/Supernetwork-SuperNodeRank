package com.example.demo.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.toolkit.StringUtils;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.demo.LoginUser;
import com.example.demo.commom.Result;
import com.example.demo.domain.entity.User;
import com.example.demo.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;


@RestController
@RequestMapping("/user")
public class UserController {
    @Resource
    UserMapper userMapper;

    @Autowired
    JavaMailSender javaMailSender;

    @Autowired
    RedisTemplate<String, Object> redisTemplate;

    //注册
    @PostMapping("/register")
    public Result<?> register(@RequestBody User user){
        User res = userMapper.selectOne(Wrappers.<User>lambdaQuery().eq(User::getUsername,user.getUsername()));
        if(res != null)
        {
            return Result.error("-1","用户名已重复");
        }else {
            //2.加密密码
            String salt = com.example.demo.utils.SHA3Util.generateRandomSalt(16);
            String pwd = com.example.demo.utils.SHA3Util.hashWithSalt(user.getPassword(), salt);
            user.setUsername(user.getUsername());
            user.setPassword(pwd);
            user.setSalt(salt);
            //3.保存用户
            userMapper.insert(user);                                                                                           ;
            return Result.success();
        }
    }

    //登录
//    @CrossOrigin
    @PostMapping("/login")
    public Result<?> login(@RequestBody User user) {
        // 1.判断用户名是否存在
        QueryWrapper<User> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("username", user.getUsername());
        User res = userMapper.selectOne(queryWrapper);
        if (res == null) {
            return Result.error("-1", "用户名不存在");
        } else {
            //2.判断密码是否正确
            String salt = res.getSalt();
            String pwd = com.example.demo.utils.SHA3Util.hashWithSalt(user.getPassword(), salt);
            if (res.getPassword().equals(pwd)) {
                //生成token
                String token = com.example.demo.utils.JwtUtil.createUserToken(res.getId(), res.getUsername(), salt);
                //返回token
                res.setToken(token);
                LoginUser loginuser = new LoginUser();
                loginuser.addVisitCount();
                return Result.success(res);
            }
        }
        return null;
    }

    @PostMapping("/sendCode")
    public Result<?> sendCode(@RequestBody Map<String, String> request) {
        String email = request.get("email");
        //根据邮箱查询数据库邮箱是否存在
        try {
            //1 创建普通邮件对象
            SimpleMailMessage message = new SimpleMailMessage();
            //收件人
            message.setTo(email);
            //发件人
            message.setFrom("2142333171@qq.com");
            //标题
            message.setSubject("图书馆系统验证码登录");
            //正文
            Random random = new Random();
            int num = random.nextInt(8999)+1000;
            message.setText("你的验证码是:");
            message.setText(num + "");
            javaMailSender.send(message);
            System.out.println("邮件发送成功");
            //把验证码存入到Redis缓存中，并设置失效时间为1分钟
            String key = "code:" + email;
            redisTemplate.opsForValue().set(key, num, 60, TimeUnit.MINUTES);


        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("邮件发送失败");
            return Result.error("-1", "验证码发送失败");
        }
        return Result.success("验证码发送成功");
    }

    @PostMapping("/loginByCode")
    public Result<?> loginByCode(@RequestBody Map<String, String> request) {
        String code = request.get("code");
        String email = request.get("email");
        System.out.println("输入的验证码:" + code);
        //验证码登录
        QueryWrapper<User> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("email", email);
        //判断邮箱对应的用户
        User user = userMapper.selectOne(queryWrapper);

        if (user == null) {
            return Result.error("-1", "用户不存在");
        } else {
            String key = "code:" + email;
            //obj就是验证码
            Object obj = redisTemplate.opsForValue().get(key);
            String salt = user.getSalt();
//            String pwd = com.example.demo.utils.SHA3Util.hashWithSalt(user.getPassword(), salt);
            if (obj == null) {
                return Result.error("-2", "验证码失效，请重新发送");
            } else {
                if (code.equals(obj + "")) {
                    //生成token
                    String token = com.example.demo.utils.JwtUtil.createUserToken(user.getId(), user.getUsername(), salt);
                    //返回token
                    user.setToken(token);
                    //user返回给前端
                    LoginUser loginuser = new LoginUser();
                    loginuser.addVisitCount();
                    return Result.success(user);
                } else {
                    return Result.error("-1", "验证码错误");
                }
            }
        }
    }


    //修改用户信息
    @PutMapping
    public  Result<?> update(@RequestBody User user){
        userMapper.updateById(user);
        return Result.success();
    }
    //删除用户
    @PostMapping("/deleteBatch")
    public  Result<?> deleteBatch(@RequestBody List<Integer> ids){
        userMapper.deleteBatchIds(ids);
        return Result.success();
    }
    @DeleteMapping("/{id}")
    public Result<?> delete(@PathVariable Long id){
        userMapper.deleteById(id);
        return Result.success();
    }
    //分页查询
    @GetMapping
    public Result<?> findPage(@RequestParam(defaultValue = "1") Integer pageNum,
                              @RequestParam(defaultValue = "10") Integer pageSize,
                              @RequestParam(defaultValue = "") String search){
        LambdaQueryWrapper<User> wrappers = Wrappers.<User>lambdaQuery();
        if(StringUtils.isNotBlank(search)){
            wrappers.like(User::getNickName,search);
        }
        wrappers.like(User::getRole,2);
        Page<User> userPage =userMapper.selectPage(new Page<>(pageNum,pageSize), wrappers);
        return Result.success(userPage);
    }
    //分页查询
    @GetMapping("/usersearch")
    public Result<?> findPage2(@RequestParam(defaultValue = "1") Integer pageNum,
                              @RequestParam(defaultValue = "10") Integer pageSize,
                              @RequestParam(defaultValue = "") String search1,
                               @RequestParam(defaultValue = "") String search2,
                               @RequestParam(defaultValue = "") String search3,
                               @RequestParam(defaultValue = "") String search4){
        LambdaQueryWrapper<User> wrappers = Wrappers.<User>lambdaQuery();
        if(StringUtils.isNotBlank(search1)){
            wrappers.like(User::getId,search1);
        }
        if(StringUtils.isNotBlank(search2)){
            wrappers.like(User::getNickName,search2);
        }
        if(StringUtils.isNotBlank(search3)){
            wrappers.like(User::getPhone,search3);
        }
        if(StringUtils.isNotBlank(search4)){
            wrappers.like(User::getAddress,search4);
        }
        wrappers.like(User::getRole,2);
        Page<User> userPage =userMapper.selectPage(new Page<>(pageNum,pageSize), wrappers);
        return Result.success(userPage);
    }

}
