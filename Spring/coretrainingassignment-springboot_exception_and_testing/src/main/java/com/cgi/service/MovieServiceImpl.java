package com.cgi.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cgi.exception.MovieAlreadyExistException;
import com.cgi.model.Movie;
import com.cgi.repository.MovieRepository;

@Service
public class MovieServiceImpl implements MovieService {

	@Autowired
	private MovieRepository movieRepo;
	
	
	public MovieServiceImpl() {
		super();
		// TODO Auto-generated constructor stub
	}

	public MovieServiceImpl(MovieRepository movieRepo) {
		super();
		this.movieRepo = movieRepo;
	}

	@Override
	public Movie saveMovie(Movie movie) throws MovieAlreadyExistException {
		if(movieRepo.existsById(movie.getId())) {
			throw new MovieAlreadyExistException();
		}
		Movie savedMovie=movieRepo.save(movie);
		return savedMovie;
	}

	@Override
	public List<Movie> getAllMovies() {
		return (List<Movie>) movieRepo.findAll();
	}

	@Override
	public void deleteMovieByid(int id) {
		movieRepo.deleteById(id);

	}

}
