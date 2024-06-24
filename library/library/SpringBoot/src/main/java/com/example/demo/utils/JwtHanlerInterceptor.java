package com.example.demo.utils;

import com.auth0.jwt.interfaces.DecodedJWT;
import com.example.demo.commom.Result;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.core.annotation.Order;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.PrintWriter;

@Order(2)
public class JwtHanlerInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        //获取token
        String token = request.getHeader("Authorization");
        //1.验证是否携带token
        if(token == null||token.isEmpty()){
            //1.设置编码格式
            response.setCharacterEncoding("utf-8");
            //2.获取打印对象
            PrintWriter pw = response.getWriter();
            //3.获取对象转换器
            ObjectMapper mapper = new ObjectMapper();
            String jason = mapper.writeValueAsString(Result.error("-1","请携带token"));
            //4.将jason字符串输出到客户端
            pw.write(jason);
            return false;
        }
        //2.验证token是否有效
        String id = com.example.demo.utils.JwtUtil.getAudience(token);
        if (id==null||id.isEmpty()){
            //1.设置编码格式
            response.setCharacterEncoding("utf-8");
            //2.获取打印对象
            PrintWriter pw = response.getWriter();
            //3.获取对象转换器
            ObjectMapper mapper = new ObjectMapper();
            String jason = mapper.writeValueAsString(Result.error("-1","token无效"));
            //4.将jason字符串输出到客户端
            pw.write(jason);
            return false;
        }
        //3.验证token是否过期
        String salt = com.example.demo.utils.JwtUtil.getClaimByName(token,"jwtSalt").asString();
        DecodedJWT decodedJWT = com.example.demo.utils.JwtUtil.verifyToken(token,salt);
        if(decodedJWT==null){
            //1.设置编码格式
            response.setCharacterEncoding("utf-8");
            //2.获取打印对象
            PrintWriter pw = response.getWriter();
            //3.获取对象转换器
            ObjectMapper mapper = new ObjectMapper();
            String jason = mapper.writeValueAsString(Result.error("-1","token过期"));
            //4.将jason字符串输出到客户端
            pw.write(jason);
            return false;
        }
        return true;
    }
}
