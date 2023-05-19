package com.cgi.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cgi.model.School;


@RestController
@RequestMapping("/api/vi")
public class SchoolController {

	@GetMapping("/school")
	public School getSchoolDetails() {
		School s1=new School();
		
		s1.setRegistrationId(101);
		s1.setSchoolName("Indian Institute of Technology");
		s1.setLocation("Guwahati");
		
		return s1;
		//return "Hey, i am in SchoolService/SchoolController";
	}
}
