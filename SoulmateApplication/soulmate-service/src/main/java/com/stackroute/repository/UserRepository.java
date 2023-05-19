package com.stackroute.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.stackroute.model.User;

public interface UserRepository extends MongoRepository<User, Integer> {

}
