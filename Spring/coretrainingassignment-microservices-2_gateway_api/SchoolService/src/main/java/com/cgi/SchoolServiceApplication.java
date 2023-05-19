package com.cgi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
/*Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * Create a following services

   1. Gateway API --- 8080
   2. SchoolService -------8081
   3. StudentService-------8082

Client Request must be accessed from the Gateway API 

 * */
@SpringBootApplication
public class SchoolServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(SchoolServiceApplication.class, args);
		System.out.println("SchoolService is running");
	}

}
