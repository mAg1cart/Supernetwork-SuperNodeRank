package com.example.demo.utils;

import org.bouncycastle.crypto.digests.SHA3Digest;
import org.bouncycastle.util.encoders.Hex;

import java.security.SecureRandom;

/**
 * 描述:SHA3 加密算法工具类
 * 时间:2024/6/12 17:18
 * 作者:admin
 * 版本:1.0
 **/
public class SHA3Util {
    /**
     * 生成加盐加密后的数据
     * @param data 需要加密的数据
     * @param salt 盐值
     * @return 加密后的数据
     */
    public static String hashWithSalt(String data, String salt) {
        byte[] input = data.getBytes();
        byte[] saltBytes = salt.getBytes();

        // 将原始数据和盐值连接起来
        byte[] dataWithSalt = new byte[input.length + saltBytes.length];
        System.arraycopy(input, 0, dataWithSalt, 0, input.length);
        System.arraycopy(saltBytes, 0, dataWithSalt, input.length, saltBytes.length);

        SHA3Digest digest = new SHA3Digest(256);
        digest.update(dataWithSalt, 0, dataWithSalt.length);

        byte[] hash = new byte[digest.getDigestSize()];
        digest.doFinal(hash, 0);

        return Hex.toHexString(hash);
    }

    /**
     * 生成盐值
     * @param length 盐值长度设定
     * @return
     */
    public static String generateRandomSalt(int length) {
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[length];
        random.nextBytes(salt);
        return Hex.toHexString(salt);
    }

    public static void main(String[] args) {
        String data = "123";
        String salt = generateRandomSalt(16);
        String hashedData = hashWithSalt(data, salt);

        System.out.println("原始密码: " + data);
        System.out.println("盐值: " + salt);
        System.out.println("加密加盐后的密码: " + hashedData);
    }
}