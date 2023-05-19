package com.stackroute.exceptions;

public class UserInfoAlreadyExistsException extends Exception {
    public UserInfoAlreadyExistsException() {
    }

    public UserInfoAlreadyExistsException(String message) {
        super(message);
    }

    public UserInfoAlreadyExistsException(String message, Throwable cause) {
        super(message, cause);
    }

    public UserInfoAlreadyExistsException(Throwable cause) {
        super(cause);
    }

    public UserInfoAlreadyExistsException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
