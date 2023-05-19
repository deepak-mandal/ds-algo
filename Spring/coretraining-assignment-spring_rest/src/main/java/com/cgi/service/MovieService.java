package com.cgi.service;

import java.util.List;

import com.cgi.model.Movie;

public interface MovieService {
	
	Movie saveMovie(Movie dept);
	List<Movie> getAllMovies();
	void deleteMovieByid(int id);
	

}
