package com.example.demo.controller;

import com.example.demo.commom.Result;
import com.example.demo.utils.Chat;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author mAg1cart
 * @date 2024/6/26 13:53
 * @description
 * @package com.example.demo.controller
 */
@RestController
@RequestMapping("/chat")
public class ChatController {


    @GetMapping
    public Result<?> AiChat(@RequestParam String question) throws Exception {
        Result<?> result=Chat.chat(question);

        return Result.success(result.getMsg());

    }

}
