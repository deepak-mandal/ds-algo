package com.cgi;

/*Write a program to read a string and a character and reverse the
 *  string and convert it in a format such that each character is 
 *  seperated by the given character. Print the final string.
 * 
 * 
 * */

import java.util.*;

public class Question5 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		System.out.print("Enter a String: ");
		String str=sc.next();		//taking the string
		System.out.print("Enter a character: ");
		char ch=sc.next().charAt(0);		//taking input as a character
		
		String outStr="";		//to store the desired result
		//logic to achieve the desired format
		for(int i=str.length()-1; i>=0; i--) {
			outStr+=Character.toString(str.charAt(i));
			if(i!=0) {
				outStr+=Character.toString(ch);
			}
		}
		
		//Displaying the desired result:-
		System.out.println("Final string: "+outStr);
		
		
	}
}
