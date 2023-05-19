package com.cgi;

/*Write a Java code to get an int array as input and identify even and odd numbers.
 *  If the number is odd, get the cube of it. If the number is even, get the
 *   square of it. Finally add all the cubes and squares together and return it as output.*/

import java.util.*;

public class Question4 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int i;
		System.out.print("Enter the size of array: ");
		int n=sc.nextInt();
		sc.nextLine();
		
		//allocating the memory for array 
		Integer arr[]=new Integer[n];
		//taking input each element and storing them into array
		for(i=0; i<n; i++) {
			System.out.print("Enter the element"+i+" of the array: ");
			arr[i]=sc.nextInt();
		}
		
		//creating evenList to store the square of element
		List evenList=new ArrayList();
		//creating oddList to store the cube of element
		List oddList=new ArrayList();
		
		//If the number is odd, get the cube of it. If the number is even, get the square of it.
		for(i=0; i<n; i++) {
			if(arr[i]%2==0) {
				evenList.add(Math.pow(arr[i], 2));
			}
			else {
				oddList.add(Math.pow(arr[i], 3));
			}
		}
		
		//adding all the cubes and squares together and return it as output.
		Double sum=0.0;
		for(Object x:evenList) {
			sum=(Double)sum+(Double)x;
		}
		
		for(Object x:oddList) {
			sum=(Double)sum+(Double)x;
		}
		//Displaying the desired result:-
		System.out.println("The Resultant sum = "+sum);
		

		
	}
}
