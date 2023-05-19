package com.cgi.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cgi.model.School;
/*Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * Create a following services

   1. Gateway API --- 8080
   2. SchoolService -------8081
   3. StudentService-------8082

Client Request must be accessed from the Gateway API 

 * */

@RestController 		//To registered as web service
public class SchoolController {
	
	@GetMapping("/school")
	public School helloSchool() {
		//creating 
		School shl = new School();
		
		shl.setSchoolName("Indian Institute of Technology");
		shl.setLocation("Guwahati, India");
		
		return shl;
		//return "Hey, I am from School service/SchoolController.java!";
	}

}
