package com.cgi.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.cgi.model.Movie;

@Repository
public interface MovieRepository extends CrudRepository<Movie, Integer> {

}
