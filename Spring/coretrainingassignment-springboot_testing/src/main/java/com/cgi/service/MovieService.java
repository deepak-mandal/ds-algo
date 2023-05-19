package com.cgi.service;

import java.util.List;

import com.cgi.exception.MovieAlreadyExistException;
import com.cgi.model.Movie;

public interface MovieService {
	
	Movie saveMovie(Movie dept) throws MovieAlreadyExistException;
	List<Movie> getAllMovies();
	void deleteMovieByid(int id);
	

}
