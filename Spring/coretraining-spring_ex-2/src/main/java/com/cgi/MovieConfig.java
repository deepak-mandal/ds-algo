package com.cgi;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MovieConfig {
	
	@Bean
	public Movie getCustomer() {
		return new Movie(101, "Bahubali", "Indian English",  9.3);
	}

}
