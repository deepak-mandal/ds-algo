package com.cgi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/* 
 * Create a following services

   1. EurekaServerService --- 8761
   2. SchoolService -------8081
   3. StudentService-------8082

 * */

@EnableDiscoveryClient
@SpringBootApplication
public class SchoolServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(SchoolServiceApplication.class, args);
		System.out.println("SchoolService is running");
	}

}
