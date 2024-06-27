package com.example.demo.controller;

import cn.hutool.core.bean.BeanUtil;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.toolkit.StringUtils;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.demo.commom.Result;
import com.example.demo.domain.dto.BookDto;
import com.example.demo.domain.entity.Book;
import com.example.demo.domain.entity.BookWithUser;
import com.example.demo.domain.entity.LendRecord;
import com.example.demo.mapper.BookMapper;
import com.example.demo.mapper.BookWithUserMapper;
import com.example.demo.mapper.LendRecordMapper;
import com.example.demo.service.BookService;
import com.example.demo.utils.ResultVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.sql.SQLOutput;
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
    BookWithUserMapper bookWithUserMapper;

    @Autowired
    BookService bookService;

    //添加
    /*@PostMapping
    public ResultVo add(@RequestBody BookDto bookDto){
        return bookService.add(bookDto);
    }*/

    //修改图书
    /*@PutMapping
    public Result<?> update(@RequestBody BookDto bookDto){
        if(bookService == null){
            System.out.println("注入失败");
            return Result.error("500","cnm");
        }
        return bookService.updateById(bookDto);
    }*/

    //根据id删除图书
    /*@DeleteMapping("{id}")
    public ResultVo delete(@PathVariable Integer id){
        return bookService.delete(id);
    }*/
    /**
     * 查询图书
     * 通过isbn,书名和作者进行搜索
     * */

    /*-----------------------------*/

    @PostMapping
    public Result<?> save(@RequestBody Book Book){
        BookMapper.insert(Book);
        return Result.success();
    }
    @PutMapping("/return")
    public  Result<?> update(@RequestBody Book Book,@RequestParam  Integer id){
        String isbn = Book.getIsbn();
        //id是用户的编号
        //需要判断这本书是不是该用户借的
        QueryWrapper<BookWithUser> wrapper = new QueryWrapper<BookWithUser>()
                .eq("isbn",isbn)
                .eq("id",id);
        BookWithUser bookWithUser = bookWithUserMapper.selectOne(wrapper);
        if(bookWithUser==null){
            return Result.error("500","您没有借这本书哦");
        }else{
            BookMapper.updateById(Book);
            return Result.success("还书成功");
        }
    }
    @PutMapping("/lend")
    public  Result<?> update(@RequestBody Book book){
        BookMapper.updateById(book);
        return Result.success("借阅成功");
    }


    //    批量删除
    @PostMapping("/deleteBatch")
    public  Result<?> deleteBatch(@RequestBody List<Integer> ids){
        BookMapper.deleteBatchIds(ids);
        return Result.success();
    }
    @DeleteMapping("/{id}")
    public Result<?> delete(@PathVariable Long id){
        BookMapper.deleteById(id);
        return Result.success();
    }
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
