package com.cgi.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.cgi.model.Movie;

public interface MovieRepository extends MongoRepository<Movie, Integer> {

}
