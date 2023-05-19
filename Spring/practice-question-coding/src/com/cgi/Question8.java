package com.cgi;

/*
 * Write a Java code to input array of numbers to find the minimum
 *  difference between 2 consecutive elements*/

import java.util.*;

public class Question8 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int i;
		
		System.out.print("Enter the size of array: ");
		int n=sc.nextInt();
		
		//creating the array object
		int arr[]=new int[n];
		//taking element and storing into the array 
		for(i=0; i<n; i++) {
			System.out.print("Enter the element"+i+" of array: ");
			arr[i]=sc.nextInt();
		}
		
		//memory allocation for the array object
		int diffArr[] =new int[n-1];
		
		//to store the difference between 2 consecutive elements
		for(i=0; i<n-1; i++) {
			diffArr[i]=Math.abs(arr[i+1]-arr[i]);
		}
		
		//just sorting the array of diffArr to get the minimum value
		Arrays.sort(diffArr);
		
		//Displaying the desired outcome:-
		System.out.println("The minimum difference between 2 consecutive elements is: "+diffArr[0]);
		
		
	}

}
