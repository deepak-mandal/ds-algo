package com.cgi.service;


import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

import java.util.ArrayList;
import java.util.List;

import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import org.springframework.boot.test.context.SpringBootTest;

import com.cgi.exception.MovieAlreadyExistException;
import com.cgi.model.Movie;
import com.cgi.repository.MovieRepository;


@SpringBootTest
@ExtendWith(MockitoExtension.class)
class MovieServiceTest {

	@Mock
	private MovieRepository mr;
	
	@InjectMocks
	private MovieServiceImpl msi;
	
	@Test
	public void TestSaveMovie() throws MovieAlreadyExistException {
		
		//fail("Not yet implemented");
		Movie m1=new Movie(110, "Science Lab - The movie", "English", 7.84);
		when(mr.save(any())).thenReturn(m1);
		msi.saveMovie(m1);
		verify(mr,times(1)).save(any());

	}
	
	@Test
	public void TestGetAllMovies() {
		
		Movie m1=new Movie(111, "Baghwan", "Hindi", 8.65);
		mr.save(m1);
		Movie m2=new Movie(112, "Machine Revolution", "English", 6.53);
		mr.save(m2);
		Movie m3=new Movie(113, "Harry Potter", "English", 8.56);
		mr.save(m3);
		
		//List object is created to store the  Movie data
		List<Movie> mList=new ArrayList<>();		
		mList.add(m1);
		mList.add(m2);
		mList.add(m3);
		
		
		when(mr.findAll()).thenReturn(mList);
		List<Movie> mList1=msi.getAllMovies();
		assertEquals(mList, mList1);
		verify(mr, times(1)).save(m1);
		verify(mr, times(1)).findAll();
		
	}
	
	
	
	
	

}
