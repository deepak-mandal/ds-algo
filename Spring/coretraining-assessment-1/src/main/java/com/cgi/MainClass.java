package com.cgi;

import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.List;
import java.util.stream.Collectors;
import com.cgi.repo.DataRepo;

/*
 3. Create a Main Class to perform the following tasks (40 Marks)
a) Extract the list of values that are multiples of 8.
b) Extract the list of names whose names does not exceed 10 characters.
c) Extract the list of names whose names starts with “C”
d) Display the StudentData who have secured more than 85 marks
e) Display the studentinfo to find a particular student.
f) Generate a infinite stream to print the numbers that are divisible by 3 and 5.
g) Create a default method to print the message “All the best” using
method reference.
h) Create a Functional interface to find the maximum among two numbers.
 * */


//Creating Functional interface :-[part of h]
interface MaxAmongTwoNo{
	//declaring the abstract method, maximum that will find the maximum among two number
	public int maximum(int x, int y);
}


//Creating functional interface "Message" :- [part of "g" of question no 3]
interface Message{
	void msg();
}


public class MainClass {
	
	//Creating a default method to print the message "All the best" :- [part of g]
	static void message() {
		System.out.println("All the best");
	}
	
	//main method of MainClass
	public static void main(String[] args) {
		
		//a) Extract the list of values that are multiples of 8.
		System.out.println("Solution of 3.a :- ");
		Arrays.stream(DataRepo.values)
		.filter(m -> m%8==0)			//checking if the value is multiples of 8
		.sorted()
		.forEach(s -> System.out.print(s+" "));
		
		
		//b) Extract the list of names whose names does not exceed 10 characters.
		System.out.println("\n\nSolution of 3.b :- ");
		DataRepo.actorNames.stream()
		.filter(n -> n.length()<10)			//checking the length of name does not exceed 10 character long
		.sorted().forEach(s1 -> System.out.print(s1+" "));
		
		
		//c) Extract the list of names whose names starts with “C”
		System.out.println("\n\nSolution of 3.c :- ");
		DataRepo.actorNames.stream()
		.filter(n -> n.startsWith("C"))			//getting the name which starts with "C" character
		.sorted().forEach(s2 -> System.out.println(s2+" "));
		
		
		//d) Display the StudentData who have secured more than 85 marks
		System.out.println("\nSolution of 3.d :- ");
		DataRepo.studentList.stream()
		.filter(sn -> sn.getMarks()>85)			//getting the student details who score more than 85 marks
		.forEach(em -> System.out.println(em));
		
		
		//e) Display the studentInfo to find a particular student.
		System.out.println("\nSolution of 3.e :- ");
		System.out.println(DataRepo.getStudentinfoByRollNo(2014));
		
		
		//f) Generate a infinite stream to print the numbers that are divisible by 3 and 5.
		System.out.println("\nSolution of 3.f :- ");
		List<Integer> numbers=IntStream.iterate(1, i -> i*3*5)
				.mapToObj(Integer::valueOf)			//converting int data type to Integer object
				.limit(10)							//infinite stream with limit of 10 numbers
				.collect(Collectors.toList());		//finally storing them in List object
		
		System.out.println(numbers+" ");

		
		//g) Create a default method to print the message “All the best” using method reference.
		System.out.println("\nSolution of 3.g :- ");
		Message printMessage = MainClass::message;		//using reference method
		printMessage.msg();
		
		
		//h) Create a Functional interface to find the maximum among two numbers.
		System.out.println("\nSolution of 3.h :- ");
		//Lambda expression to find the maximum among two numbers using functional interface.
		MaxAmongTwoNo max= (x, y) -> x>y?x:y;
		
		int result=max.maximum(20, 30);
		//Displaying the desired result
		System.out.println("Maximum among two numbers 20 & 30 is: "+result);
		
		
		
	}
}
