package com.example.demo.domain.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.io.Serializable;
/**
 * @author mAg1cart
 * @date 2024/6/21 19:50
 * @description 图书实体类
 * @package com.example.demo.domain.entity
 */

@TableName("user")
@Data
public class User implements Serializable {
    @TableId (type = IdType.AUTO)
    private Integer id;
    private String username;
    private String nickName;
    private String password;
    private String sex;
    private String address;
    private String phone;
    @TableField(exist = false)  //表中没有token不会报错仍能编译运行
    private String token;
    private Integer role;
    @TableField(exist = false)
    private Integer delete_flag;

}
