package com.example.demo.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.example.demo.domain.dto.BookDto;
import com.example.demo.domain.entity.Book;
import com.example.demo.domain.entity.User;
import com.example.demo.utils.ResultVo;

/**
 * @author mAg1cart
 * @date 2024/6/21 19:46
 * @description
 * @package com.example.demo.service
 */
public interface BookService extends IService<Book> {
    /**
     * 新增图书
     * */
    ResultVo add(BookDto bookDto);

    /**
     * 修改图书信息
     * */
    ResultVo update(BookDto bookDto);

    /**
     * 删除图书
     * */
    ResultVo delete(Integer id);

    /**
     * 查询图书信息
     * */
    ResultVo query(BookDto bookDto);


}
