package com.cgi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

/* 
 * Create a following services

   1. EurekaServerService --- 8761
   2. SchoolService -------8081
   3. StudentService-------8082



In microservice -> all the microservice is linked with "EurekaServer"
-> and all the microservice is communicating to each other & has a copy of data so no won't be failure even if the one of the server is down

while creating project add 1. spring web, 2. eureka server


port no of eureka server is 8761
client application & will register the eureka server




for clent service -> will get registered with eureka server
while creating project add 1. spring web 2. eureka discovery client



in client service => @EurekaDiscoveryClient





 * */

@EnableEurekaServer
@SpringBootApplication
public class EurekaServerServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(EurekaServerServiceApplication.class, args);
		System.out.println("EurekaServerService is running");
	}

}
