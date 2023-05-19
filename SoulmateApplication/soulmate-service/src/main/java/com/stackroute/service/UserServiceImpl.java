package com.stackroute.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.stackroute.model.User;
import com.stackroute.repository.UserRepository;

@Service
public class UserServiceImpl implements UserService {


    private UserRepository userRepository;


    public UserServiceImpl() {
        super();
        // TODO Auto-generated constructor stub
    }

    @Autowired
    public UserServiceImpl(UserRepository userRepository) {
        super();
        this.userRepository = userRepository;
    }

    @Override
    public User saveUser(User user) {
        User savedUser=userRepository.save(user);
        return savedUser;
    }
<<<<<<< HEAD

=======
/*
    @Override
    public List<User> getAllMovies() {
        return (List<User>) movieRepo.findAll();
    }

    @Override
    public void deleteMovieByid(int id) {
        movieRepo.deleteById(id);

    }
*/
>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b
}
