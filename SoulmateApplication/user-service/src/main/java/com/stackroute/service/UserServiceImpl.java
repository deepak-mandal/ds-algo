package com.stackroute.service;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.stackroute.model.User;
import com.stackroute.repository.UserRepository;

@Service("UserService")
public class UserServiceImpl implements UserService{

    @Autowired
    private UserRepository userRepository;


    public boolean save(User user) {
        return (userRepository.save(user) != null);
    }


    public boolean update(User user) {
        return (userRepository.save(user) != null);
    }



    public boolean delete(User user) {
        userRepository.delete(user);
        if (userRepository.findById(user.getEmail()) != null) {
            return false;
        } else
            return true;
    }



    //for Read operation
    public List<User> list() {
        return (List<User>) userRepository.findAll();
    }



    public boolean validate(String email, String password) {

        if (userRepository.validate(email, password) != null) {
            return true;
        }
        else {
            return false;
        }
    }



    public User get(String email) {
        return userRepository.findById(email).get();
    }



    public boolean exists(String email) {
        return userRepository.existsById(email);
    }






}