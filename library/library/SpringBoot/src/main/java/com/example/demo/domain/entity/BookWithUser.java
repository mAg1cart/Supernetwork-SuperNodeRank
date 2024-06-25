package com.example.demo.domain.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableLogic;
import com.baomidou.mybatisplus.annotation.TableName;
import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;
/**
 * @author mAg1cart
 * @date 2024/6/21 19:46
 * @description 借阅状态,查询所有书的信息
 * @package com.example.demo.domian.entity
 */
@TableName("bookwithuser")
@Data
public class BookWithUser implements Serializable {

    private Integer id;
    private String isbn;
    private String bookName;
    private String nickName;
    @JsonFormat(locale="zh",timezone="GMT+8", pattern="yyyy-MM-dd HH:mm:ss")
    private Date lendtime;
    @JsonFormat(locale="zh",timezone="GMT+8", pattern="yyyy-MM-dd HH:mm:ss")
    private Date deadtime;
    private Integer prolong;
    @TableField(value = "delete_flag")
    @TableLogic(value = "0",delval = "1")
    private Integer deleteFlag;

}
