package com.stackroute.service;


import java.util.List;

import com.stackroute.model.User;

public interface UserService {

    public boolean save(User user);
    public boolean update(User user);
    public boolean delete(User user);
    public List<User> list();

    public boolean validate(String email, String password);

    public User get(String email);
    public boolean exists(String email);





}
