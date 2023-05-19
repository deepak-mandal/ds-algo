package com.cgi.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cgi.model.Student;
/*Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * Create a following services

   1. Gateway API --- 8080
   2. SchoolService -------8081
   3. StudentService-------8082

Client Request must be accessed from the Gateway API 

 * */
@RestController
public class StudentController {
	
	@GetMapping("/student")
	public Student getProdDetails() {
		//instantiating the object
		Student stud= new Student();
		
		stud.setRollno(2014);
		stud.setName("Deepak");
		stud.setDepartment("Software");
		stud.setFee(111111.11);
		
		return stud;
	}
	
	
	

}
