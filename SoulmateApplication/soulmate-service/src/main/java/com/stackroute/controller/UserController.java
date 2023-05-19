package com.stackroute.controller;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


import com.stackroute.model.User;
import com.stackroute.service.UserService;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/vi")
public class UserController {


	private UserService userService;

	@Autowired
	public UserController(UserService userService) {
		this.userService = userService;
	}

	//To perform Create operation
	@PostMapping("/mvi")
	public ResponseEntity<User> saveUser(@RequestBody User user){
		User saveduser = userService.saveUser(user);
		return new ResponseEntity<>(saveduser, HttpStatus.CREATED);

	}

<<<<<<< HEAD
=======
	/*
	//To perform Read operation
	@GetMapping("/mvis")
	public ResponseEntity<List<User>> getAllDepartments(){
		return new ResponseEntity<List<User>>((List<User>)movieServ.getAllMovies(), HttpStatus.OK);
	}

	//To perform Delete operation
	@DeleteMapping("/mvi/{id}")
	public ResponseEntity<Void> deleteMovieById(@PathVariable int id){
		movieServ.deleteMovieByid(id);
		return ResponseEntity.noContent().build();
	}
*/

>>>>>>> d7a6b7188563d9b8c122c24bf1c061bd508bea9b



}
