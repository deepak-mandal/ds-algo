package com.cgi;

/*
 * 5. Create a Movie class with the following Attributes
      movirId, movieName, language, rating.
   Create a Config class to configure the MovieBean
   Create a MovieMain to to display the details of the Movies
 * */

public class Movie {
	
	private int movieId;
	private String movieName;
	private String language;
	private double rating;
	
	public Movie() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Movie(int movieId, String movieName, String language, double rating) {
		super();
		this.movieId = movieId;
		this.movieName = movieName;
		this.language = language;
		this.rating = rating;
	}

	public int getMovieId() {
		return movieId;
	}

	public void setMovieId(int movieId) {
		this.movieId = movieId;
	}

	public String getMovieName() {
		return movieName;
	}

	public void setMovieName(String movieName) {
		this.movieName = movieName;
	}

	public String getLanguage() {
		return language;
	}

	public void setLanguage(String language) {
		this.language = language;
	}

	public double getRating() {
		return rating;
	}

	public void setRating(double rating) {
		this.rating = rating;
	}

	@Override
	public String toString() {
		return "Movie [movieId=" + movieId + ", movieName=" + movieName + ", language=" + language + ", rating="
				+ rating + "]";
	}
	
	

}
