package com.example.demo.service.impl;

import cn.hutool.core.bean.BeanUtil;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.demo.domain.dto.BookDto;
import com.example.demo.domain.entity.Book;

import com.example.demo.mapper.BookMapper;
import com.example.demo.service.BookService;
import com.example.demo.utils.ResultVo;
import org.springframework.dao.DataAccessException;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.HashMap;
import java.util.Map;

/**
 * @author mAg1cart
 * @date 2024/6/21 20:47
 * @description
 * @package com.example.demo.service.impl
 */

@Service
public class BookServiceImpl extends ServiceImpl<BookMapper, Book> implements BookService {
    @Resource
    BookMapper bookMapper;


    /**
     * 新增图书
     * */
    @Override
    public ResultVo add(BookDto bookDto) {
        Book book = BeanUtil.copyProperties(bookDto, Book.class);
        try {
            int num = bookMapper.insert(book);
            if (num > 0) {
                return ResultVo.success();
            } else {
                return ResultVo.error();
            }
        } catch (DataAccessException e) { //DataAccessException抛出sql语句的异常
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResultVo.error();
    }

    /**
     * 修改图书
     * */
    @Override
    public ResultVo update(BookDto bookDto) {
        Book book = BeanUtil.copyProperties(bookDto, Book.class);
        int num = bookMapper.updateById(book);
        if(num > 0) {
            return ResultVo.success();
        }
        return ResultVo.error();
    }

    @Override
    public ResultVo delete(Integer id) {
        int num = bookMapper.deleteById(id);
        if(num > 0) {
            return ResultVo.success();
        }
        return ResultVo.error();
    }

    @Override
    public ResultVo query(BookDto bookDto) {
        Page<Book> page = new Page<>(bookDto.getPage(), bookDto.getRow());




        Map<String, Object> map = new HashMap<>();
        //当前页数
        map.put("list", page.getRecords());
        //总条数
        map.put("total", page.getTotal());
        //总页数
        map.put("totalPages", page.getPages());
        if (page.getRecords().size() > 0) {
            return ResultVo.success("查询到数据", map);
        }


        return ResultVo.error();
    }
}
