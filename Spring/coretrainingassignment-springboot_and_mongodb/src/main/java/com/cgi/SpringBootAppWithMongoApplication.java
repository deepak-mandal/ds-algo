package com.cgi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringBootAppWithMongoApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootAppWithMongoApplication.class, args);
		System.out.println("SpringBootAppWithMongoDB");
	}

}
