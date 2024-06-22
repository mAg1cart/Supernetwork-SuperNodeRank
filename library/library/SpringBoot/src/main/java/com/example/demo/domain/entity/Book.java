package com.example.demo.domain.entity;

/*实体类*/
/**
 * @author mAg1cart
 * @date 2024/6/21 19:46
 * @description 图书实体类
 * @package com.example.demo.domian.entity
 */
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.Data;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.Date;

@TableName("book")
@Data
public class Book implements Serializable {

    @TableId (type = IdType.AUTO)
    private Integer id;
    private String isbn;
    private String name;
    private BigDecimal price;
    private String author;
    private Integer borrownum;
    private String publisher;
    @JsonFormat(locale="zh",timezone="GMT+8", pattern="yyyy-MM-dd")
    private Date createTime;
    private String status;
    /**
     * 假删,0正常,1删除
     * */
    @TableField(value = "delete_flag")
    private Integer deleteFlag;

}
