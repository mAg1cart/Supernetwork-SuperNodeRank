package com.example.demo.utils;

import lombok.Data;

/**
 * @author mAg1cart
 * @date 2024/6/21 20:29
 * @description 返回结果
 * @package com.example.demo.utils
 */
@Data
public class ResultVo {
    public ResultVo(Integer code, String msg, Object data) {
        this.code = code;
        this.msg = msg;
        this.data = data;
    }

    /**
     * 状态码
     * 200成功,500失败
     * */
    private Integer code;

    /**
     * 提示信息
     * */
    private String msg;

    /**
     * 数据
     * 用父类,
     * */
    private Object data;

    /**
     * 成功方法
     * */
    public static ResultVo success(){
        return new ResultVo(200,"success",null);
    }

    public static ResultVo success(String msg,Object data){
        return new ResultVo(200,msg,data);
    }

    /**
     * 失败方法
     * */
    public static ResultVo error(){
        return new ResultVo(500,"failure",null);
    }

    public static ResultVo error(String msg,Object data){
        return new ResultVo(500, msg,data);
    }
}
