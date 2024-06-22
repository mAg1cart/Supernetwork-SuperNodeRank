package com.example.demo.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.toolkit.StringUtils;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.demo.commom.Result;
import com.example.demo.domain.dto.BookDto;
import com.example.demo.domain.entity.Book;
import com.example.demo.mapper.BookMapper;
import com.example.demo.service.BookService;
import com.example.demo.utils.ResultVo;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;
/**
 * @author mAg1cart
 * @date 2024/6/21 20:01
 * @description
 * @package com.example.demo.controller
 */
@RestController
@RequestMapping("/book")
public class BookController {
    @Resource
    BookMapper BookMapper;

    @Resource
    BookService bookService;

    //添加
    @PostMapping
    public ResultVo add(@RequestBody BookDto bookDto){
        return bookService.add(bookDto);
    }

    //修改图书
    @PutMapping
    public ResultVo update(@RequestBody BookDto bookDto){
        return bookService.update(bookDto);
    }

    //根据id删除图书
    @DeleteMapping("{id}")
    public ResultVo delete(@RequestParam Integer id){
        return bookService.delete(id);
    }
    /**
     * 查询图书
     * 通过isbn,书名和作者进行搜索
     * */

    /*-----------------------------*/

    /*@PostMapping
    public Result<?> save(@RequestBody Book Book){
        BookMapper.insert(Book);
        return Result.success();
    }*/
    /*@PutMapping
    public  Result<?> update(@RequestBody Book Book){
        BookMapper.updateById(Book);
        return Result.success();
    }*/

    //    批量删除
    @PostMapping("/deleteBatch")
    public  Result<?> deleteBatch(@RequestBody List<Integer> ids){
        BookMapper.deleteBatchIds(ids);
        return Result.success();
    }
    /*@DeleteMapping("/{id}")
    public Result<?> delete(@PathVariable Long id){
        BookMapper.deleteById(id);
        return Result.success();
    }*/
    @GetMapping
    public Result<?> findPage(@RequestParam(defaultValue = "1") Integer pageNum,
                              @RequestParam(defaultValue = "10") Integer pageSize,
                              @RequestParam(defaultValue = "") String search1,
                              @RequestParam(defaultValue = "") String search2,
                              @RequestParam(defaultValue = "") String search3){
        LambdaQueryWrapper<Book> wrappers = Wrappers.<Book>lambdaQuery();
        if(StringUtils.isNotBlank(search1)){
            wrappers.like(Book::getIsbn,search1);
        }
        if(StringUtils.isNotBlank(search2)){
            wrappers.like(Book::getName,search2);
        }
        if(StringUtils.isNotBlank(search3)){
            wrappers.like(Book::getAuthor,search3);
        }
        Page<Book> BookPage =BookMapper.selectPage(new Page<>(pageNum,pageSize), wrappers);
        return Result.success(BookPage);
    }

}
