package com.cgi.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cgi.model.Student;

@RestController
@RequestMapping("/api/vi")
public class StudentController {
	
	@GetMapping("/student")
	public Student getStudentDetails() {
		Student e1=new Student(2014, "Deepak");
		return e1;
		//return "Welcome to Eureka Client App. - EmployeeService/EmployeeController";
	}

}
