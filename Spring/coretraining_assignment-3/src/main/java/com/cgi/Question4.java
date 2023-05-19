package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 4. Create a infinite Stream that prints multiples of 9
 * */

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Question4 {
	
	public static void main(String args[]) {
		
		List<Integer> numbers = IntStream.iterate(1, i->i*9)		//'i' will iterate and give outputs multiples of 9
				.mapToObj(Integer::valueOf)		//Convert int data type to Integer Object
				.limit(10)						//It limits the no. of elements in the output
				.collect(Collectors.toList());	//Storing all the element into the List Object
		
		//Printing the desired result
		System.out.println(numbers+" ");
		
	}
}
