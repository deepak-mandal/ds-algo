package com.stackroute.controller;

import com.stackroute.exceptions.UserInfoAlreadyExistsException;
import com.stackroute.model.UserInfo;
import com.stackroute.service.MatchingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("api/v1")
public class MatchingController {
    private MatchingService matchingService;

    public MatchingController(MatchingService matchingService) {
        this.matchingService = matchingService;
    }

    @PostMapping("")
    public ResponseEntity<?> addUserInfoNode(@RequestBody UserInfo userInfo) throws UserInfoAlreadyExistsException {
        this.matchingService.processUserNode(userInfo);
        return ResponseEntity.noContent().build();
    }

}
