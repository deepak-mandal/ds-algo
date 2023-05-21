package com.cgi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringRestAppApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringRestAppApplication.class, args);
		System.out.println("Spring Boot - Movie Application!");
	}

}
