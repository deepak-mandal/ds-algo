package com.cgi.repo;

import java.util.Arrays;
import java.util.List;
import com.cgi.Model.Student;

/*
 2. Create a Data Repos to do the following (5 Marks)
a) Create a Integer Array to store 15 values.
b) Create a List of names of Actors
c) Create a studentList to store array of Student Objects.
 * */

public class DataRepo {
	
	//a) Creating a Integer Array to store 15 values.
	public static int values[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16};
	
	//b) Creating a List of names of Actors
	public static List<String> actorNames = Arrays.asList("Chetan", "Aamir", "Ajay ", "Shah Rukh", "Ryan Reynolds", "Chris Pine");
	
	//c) Creating a studentList to store array of Student Objects.
	public static List<Student> studentList = Arrays.asList( new Student[] {
			new Student(2014, "Deepak Kumar Mandal", 100, 9.99),
			new Student(2015, "Deekshant", 90, 8.09),
			new Student(2016, "Devansi", 80, 7.90),
			new Student(2041, "Mayank", 89, 9.91),
			new Student(2043, "Shayam Prasad", 79, 7.33)
	});
	
	//creating getStudentinfoByRollNo() method that required for question 3.e
	public static Student getStudentinfoByRollNo(int rollNo) {
		return studentList.stream().filter(s -> s.getRollno()==rollNo).findAny().get();
	}

}
