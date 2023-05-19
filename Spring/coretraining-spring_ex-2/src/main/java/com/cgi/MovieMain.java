package com.cgi;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MovieMain {
	public static void main(String[] args) {
		//AnnotationConfigApplication Context - using class based configuaration
		ApplicationContext ctx = new AnnotationConfigApplicationContext(MovieConfig.class);
		Movie movie = ctx.getBean(Movie.class);
		
		movie.setMovieId(102);
		movie.setMovieName("Don");
		movie.setLanguage("Hindi");
		movie.setRating(7.13);
		
		
		System.out.println(movie);
	}

}
