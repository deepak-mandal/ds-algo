package com.stackroute.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.stream.annotation.EnableBinding;
import org.springframework.integration.support.MessageBuilder;
import org.springframework.web.bind.annotation.*;

import com.stackroute.model.UserLogin;
import com.stackroute.source.UserRegistrationSource;

@RestController
@CrossOrigin("*")
@EnableBinding(UserRegistrationSource.class)
public class UserRegistrationController {

    @Autowired
    UserRegistrationSource userRegistrationSource;

    @RequestMapping("/register")
    @ResponseBody
    public String sendUser(@RequestBody UserLogin user) {
        userRegistrationSource.userRegistration().send(MessageBuilder.withPayload(user).build());
        System.out.println(user.toString());
        System.out.println("Email= "+ ((Object)user).getClass().getSimpleName());
        System.out.println("Email= "+user.getEmail());
        System.out.println("Password= "+user.getPassword());
        return "User Registered Successfully!";
    }

}
