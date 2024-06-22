package com.example.demo;

/**
 * @author mAg1cart
 * @date 2024/6/22 19:46
 * @description
 * @package com.example.demo.service
 */

/*访问数*/

public class LoginUser {
    private static int visitCount = 0;
    /**
     * 记录访问数
     * */
    public static void addVisitCount() {
        LoginUser.visitCount++;
    }
    /**
     * 获取访问数
     * */
    public static int getVisitCount() {
        return LoginUser.visitCount;
    }

}
