package com.cgi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

/* 
 * Create a following services

   1. EurekaServerService --- 8761
   2. SchoolService -------8081
   3. StudentService-------8082

 * */

@EnableEurekaServer
@SpringBootApplication
public class EurekaServerServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(EurekaServerServiceApplication.class, args);
		System.out.println("EurekaServerService is running");
	}

}
