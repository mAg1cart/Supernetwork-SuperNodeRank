package com.example.demo.utils;

import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.interfaces.Claim;
import com.auth0.jwt.interfaces.DecodedJWT;
import com.auth0.jwt.interfaces.JWTVerifier;

import java.util.Date;
import java.util.UUID;

/**
 * @Description
 * @Autor 伍军
 * @Date 2022/5/30 10:18
 * @Version 1.0
 **/
public class JwtUtil {

    //设置过期为1小时，单位：毫秒
    private static final Long EXPIRES_TIME = 1 * 60 * 60 * 1000L;


    /**
     * -创建用户令牌
     * @param id      JWT 唯一身份标识，使用 userId、UUID 等
     * @param userName 用户名，自定义载荷内容
     * @param jwtSalt 盐值
     * @return token
     */
    public static String createUserToken(String id, String userName,String jwtSalt) {
        //获取当前时间 作为签发时间
        Date currentDate = new Date();
        //生成有效期，作为 Token的有效期
        Date expDate = new Date(System.currentTimeMillis() + EXPIRES_TIME);
        //使用 HMAC256 加密算法，生成签名
        Algorithm signName = Algorithm.HMAC256(jwtSalt);
        return JWT.create().withAudience(id) // 签发对象
                .withIssuedAt(currentDate) // 发行时间
                .withExpiresAt(expDate) // 有效期
                .withClaim("userName", userName) // Payload 载荷，可按官方推荐，也可自定义，可有多个
                .withClaim("jwtSalt", jwtSalt) // 这里存入盐值，是为了后续其他功能 需要取盐值操作的
                .sign(signName);

    }

    /**
     * - 获取令牌中的签发对象: 就是JWT.create().withAudience(id) 的id值
     */
    public static String getAudience(String token) {
        String audience = null;
        try {
            audience = JWT.decode(token).getAudience().get(0);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return audience;

    }

    /**
     * 用签发对象验证令牌
     * @param token 要盐值的token
     * @param jwtSalt 要盐值的token的盐值
     * @return
     */
    public static DecodedJWT verifyToken(String token, String jwtSalt) {
        DecodedJWT decodedJWT = null;
        try {
            JWTVerifier jWTVerifier = JWT.require(Algorithm.HMAC256(jwtSalt)).build();
            decodedJWT = jWTVerifier.verify(token);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return decodedJWT;
    }

    /**
     * - 根据名字获取载荷内容  withClaim("userName", userName)
     */
    public static Claim getClaimByName(String token, String claimName) {
        return JWT.decode(token).getClaim(claimName);

    }

    public static void main(String[] args) {
        //盐值
        String jwtSalt = UUID.randomUUID()+"";
        //id表示
        String id = UUID.randomUUID()+"";
        String token = JwtUtil.createUserToken(id,"cat",jwtSalt);
        System.out.println(token);
        System.out.println("验证码token是否正确 正确：实体对象，错误：null "+JwtUtil.verifyToken(token, jwtSalt));
        System.out.println("id值:"+JwtUtil.getAudience(token));
        System.out.println("盐值:"+JwtUtil.getClaimByName(token, "jwtSalt"));
        System.out.println("获取token中的用户名:"+JwtUtil.getClaimByName(token,"userName"));

    }

}