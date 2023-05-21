package com.cgi.repository;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import com.cgi.model.Movie;

@ExtendWith(SpringExtension.class)
@SpringBootTest
class MovieRepositoryTest {
	
	@Autowired
	private MovieRepository movieRepo;

	@Test
	public void givenMovieShouldReturnMovieObjectTest() {
		//fail("Not yet implemented");
		//User Input
		Movie m1=new Movie(1001, "MovieTesting - Engineering", "English", 9.32);
		//Data is saved into Database
		movieRepo.save(m1);
		//Data is retrieved from database
		Movie m2 = movieRepo.findById(m1.getId()).get();
		assertNotNull(m2);
		assertEquals(m1.getName(), m2.getName());
			
	}
	
	
	@Test
	public void getAllMustReturnAllMovies() {
		//Two user inputs m3, m4;
		Movie m3=new Movie(1002, "Parallel Universe", "English", 8.33);
		Movie m4=new Movie(1003, "Tere Naam", "Hindi", 7.5);
		
		//Saving the data in to database
		movieRepo.save(m3);
		movieRepo.save(m4);
		
		List<Movie> movieList = (List<Movie>) movieRepo.findAll();
		assertEquals("Tere Naam", movieList.get(5).getName());
	}
	
	
	

}
