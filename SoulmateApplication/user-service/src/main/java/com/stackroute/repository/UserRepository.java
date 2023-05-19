package com.stackroute.repository;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.stackroute.model.User;

@Repository
public interface UserRepository extends CrudRepository<User, String> {

    @Query("select u from User u where u.email = (?1) and u.password = (?2)")
    User validate(String email,String password);
}
