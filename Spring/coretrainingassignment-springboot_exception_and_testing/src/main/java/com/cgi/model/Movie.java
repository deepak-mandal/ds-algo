package com.cgi.model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

//Model class for performing CRUD operation - Movie

@Entity
@Table(name="movies")
public class Movie {
	
	@Id
	private int id;
	private String name;
	private String language;
	private double rating;
	
	public Movie() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Movie(int id, String name, String language, double rating) {
		super();
		this.id = id;
		this.name = name;
		this.language = language;
		this.rating = rating;
	}

	//getter and setters method
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
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
	
	

	
	
	
}
