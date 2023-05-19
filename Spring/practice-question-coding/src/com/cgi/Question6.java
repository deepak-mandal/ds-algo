package com.cgi;

/*Write a Java program to find the input string is palindrome or not.
 * 
 * */

import java.util.*;

public class Question6 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Enter a string: ");
		String str=sc.next();
		
		//creating the StringBuffer object - for mutable string
		StringBuffer sb=new StringBuffer(str);
		
		//just reversing the string
		sb.reverse();
		//Converting the StringBuffer object to String object
		String revStr=sb.toString();
		
		//to display the desired result:-
		if(str.equalsIgnoreCase(revStr)) {
			System.out.println("The input string is Palindrome.");
		}
		else {
			System.out.println("The input string is not a Palindrome.");
		}
		
	}
}
