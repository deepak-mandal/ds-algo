package com.cgi.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


import com.cgi.model.Movie;
import com.cgi.service.MovieService;

@RestController
@RequestMapping("/api/vi")
public class MovieController {
	
	
	private MovieService movieServ;

	@Autowired
	public MovieController(MovieService movieServ) {
		this.movieServ = movieServ;
	}
	
	//To perform Create operation
	@PostMapping("/mvi")
	public ResponseEntity<Movie> saveMovie(@RequestBody Movie movie){
		Movie savedmovie = movieServ.saveMovie(movie);
		return new ResponseEntity<>(savedmovie, HttpStatus.CREATED);
	
	}
	
	//To perform Read operation
	@GetMapping("/mvis")
	public ResponseEntity<List<Movie>> getAllDepartments(){
		return new ResponseEntity<List<Movie>>((List<Movie>)movieServ.getAllMovies(), HttpStatus.OK);
	}
	
	//To perform Delete operation
	@DeleteMapping("/mvi/{id}")
	public ResponseEntity<Void> deleteMovieById(@PathVariable int id){
		movieServ.deleteMovieByid(id);
		return ResponseEntity.noContent().build();
	}
	
	
	
	

}

