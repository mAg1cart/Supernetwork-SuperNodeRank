package com.example.demo.domain.entity;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

@TableName("user")
@Data
public class User {
    @TableId (type = IdType.AUTO)
    private String id;
    private String username;
    private String nickName;
    private String password;
    private String sex;
    private String address;
    private String phone;
    @TableField(exist = false)  //表中没有token不会报错仍能编译运行
    private String token;
    private Integer role;
    private String salt;
    @TableLogic(value="0",delval="1")//未删除0 删除1
    private String deleteFlag;
}
