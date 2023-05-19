package com.stackroute.exceptions;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(UserInfoAlreadyExistsException.class)
    public ResponseEntity<String> handleUserInfoAlreadyExists(UserInfoAlreadyExistsException e) {
        return new ResponseEntity<>("Another Node with same ID already exists!", HttpStatus.CONFLICT);
    }
}
