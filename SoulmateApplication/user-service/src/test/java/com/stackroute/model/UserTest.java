package com.stackroute.model;

public class UserTest {

    private String email;
    private String password;

    public UserTest(String email, String password) {
        this.email = email;
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }

}
