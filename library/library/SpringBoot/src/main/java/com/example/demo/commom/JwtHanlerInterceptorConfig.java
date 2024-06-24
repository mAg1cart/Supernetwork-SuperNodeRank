package com.example.demo.commom;

import com.example.demo.utils.JwtHanlerInterceptor;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class JwtHanlerInterceptorConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new JwtHanlerInterceptor())
                .addPathPatterns("/**")
                .excludePathPatterns("/**");//拦截所有请求，排除登录请求
    }
}
