package com.cgi;

/*
 * 1. Write a Java code to find the Happy Number*/

import java.util.*;

public class Question1 {
	public static int isHappyNumber(int num) {
		int rem=0, sum=0;		//for storing reminder & sum of square of its digits
		
		//calculating sum of square of digit
		while(num>0) {
			rem=num%10;
			sum=sum+(rem*rem);
			num=num/10;
		}
		return sum;
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		System.out.print("Enter any number: ");
		int n=sc.nextInt();
		
		int result=n;
		
		/*The happy number can be defined as a number which will yield 1 when it 
		is replaced by the sum of the square of its digits repeatedly. If this 
		process results in an endless cycle of numbers containing 4, then the 
		number is called an unhappy number.*/
		while(result!=1 && result!=4) {
			result=isHappyNumber(result);
		}
		
		//Displaying the desired result:
		if(result==1) {
			System.out.println(n+" is a Happy number");
		}
		else if(result==4) {
			System.out.println(n+" is not a Happy Number");
		}
	
		
	}
}
