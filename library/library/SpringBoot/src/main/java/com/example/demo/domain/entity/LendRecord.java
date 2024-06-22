package com.example.demo.domain.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;
/**
 * @author mAg1cart
 * @date 2024/6/21 19:46
 * @description 借阅信息,用户自己借的书
 * @package com.example.demo.domain.entity
 */

@TableName("lend_record")
@Data
public class LendRecord implements Serializable {
    private Integer readerId;
    private String isbn;
    private String bookname;
    @JsonFormat(locale="zh",timezone="GMT+8", pattern="yyyy-MM-dd HH:mm:ss")
    private Date lendTime;
    @JsonFormat(locale="zh",timezone="GMT+8", pattern="yyyy-MM-dd HH:mm:ss")
    private Date returnTime;
    private String status;
    private Integer borrownum;
    @TableField(value = "delete_flag")
    private Integer deleteFlag;


}
