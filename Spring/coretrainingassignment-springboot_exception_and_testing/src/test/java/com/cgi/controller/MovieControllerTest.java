package com.cgi.controller;


import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultHandlers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import com.cgi.model.Movie;
import com.cgi.service.MovieService;
import com.fasterxml.jackson.databind.ObjectMapper;

@ExtendWith(MockitoExtension.class)
class MovieControllerTest {

	@Autowired
	private MockMvc mockMvc;
	
	@Mock
	private MovieService movieService;
	private Movie movie;
	private List<Movie> movieList;
	
	@InjectMocks
	private MovieController movieController;
	
	@BeforeEach
	public void setUp() {
		movie=new Movie(10001, "Technology War", "English", 9.99);
		mockMvc=MockMvcBuilders.standaloneSetup(movieController).build();
	}
	
	
	@Test
	public void saveMovieControllerTest() throws Exception {
		when(movieService.saveMovie(any())).thenReturn(movie);
		mockMvc.perform(post("/api/vi/mvi")
				.contentType(MediaType.APPLICATION_JSON)
				.content(asJsonString(movie)))
		.andExpect(status().isCreated());
		verify(movieService, times(1)).saveMovie(any());		

	}
	
	
	private static String asJsonString(final Object obj) {
		// TODO Auto-generated method stub
		try {
			return new ObjectMapper().writeValueAsString(obj);
		}
		catch(Exception e) {
			throw new RuntimeException(e);
		}
	}
	
	
	@Test
	public void getAllMoviesControllerTest() throws Exception{
		when(movieService.getAllMovies()).thenReturn(movieList);
		mockMvc.perform(MockMvcRequestBuilders.get("/api/vi/mvis")
				.contentType(MediaType.APPLICATION_JSON)
				.content(asJsonString(movie)))
		.andDo(MockMvcResultHandlers.print());
		verify(movieService, times(1)).getAllMovies();
		
	}
	
	

}


