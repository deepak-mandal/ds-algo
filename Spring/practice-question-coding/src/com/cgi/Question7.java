package com.cgi;

/*Write a Java code to input array of numbers to find the maximum
 *  difference between 2 consecutive elements
 * 
 * */

import java.util.*;

public class Question7 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int i;	//to store the index of array for iterating purpose
		
		System.out.print("Enter the size of array: ");
		int n=sc.nextInt();
		
		int arr[]=new int[n];		//memory allocation
		//taking element as input and storing into array
		for(i=0; i<n; i++) {
			System.out.print("Enter the element"+i+" of array: ");
			arr[i]=sc.nextInt();
		}
		
		//Allocation of memory for array 
		int diffArr[] =new int[n-1];
		
		//to store the difference between 2 consecutive elements
		for(i=0; i<n-1; i++) {
			diffArr[i]=Math.abs(arr[i+1]-arr[i]);		//taking the absolute value
		}
		
		//sorting the diffArr to get the maximum difference
		Arrays.sort(diffArr);
		
		//Displaying the desired result:-
		System.out.println("The maximum difference between 2 consecutive elements is: "+diffArr[n-2]);
		
	}
}
