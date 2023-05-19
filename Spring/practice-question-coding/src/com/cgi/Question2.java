package com.cgi;

/*Write a Java code to input elements for 2 different arrays. Find the sum
 *  of the common elements */

import java.util.*;

public class Question2 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int i, n1, n2;	//n1: for size of array1 & n2: to store size of array2
		
		System.out.print("Enter the length of Array 1: ");
		n1=sc.nextInt();
		sc.nextLine();
		
		int arr1[]=new int[n1];
		//taking input each element and storing them into array1
		for(i=0; i<n1; i++) {
			System.out.print("Enter element"+i+" of the array1: ");
			arr1[i]=sc.nextInt();
		}
		
		System.out.print("Enter the length of Array 2: ");
		n2=sc.nextInt();
		sc.nextLine();
		
		int arr2[]=new int[n2];
		//taking input element of int data type and storing them into array2 
		for(i=0; i<n2; i++) {
			System.out.print("Enter the element"+i+" of array2: ");
			arr2[i]=sc.nextInt();
		}
		
		//Just printing the both array
		System.out.print("\nArray1: ");
		for(int x: arr1) {
			System.out.print(x+" ");
		}
		System.out.print("\nArray2: ");
		for(int x: arr2) {
			System.out.print(x+" ");
		}
		
		//just sorting the both array
		Arrays.sort(arr1);	
		Arrays.sort(arr2);
		
		int sum=0;		//to store the sum of common element
		//to find the sum of the common elements
		for(i=0; i<n1; i++) {
			int count=0;
			for(int j=0; j<n2; j++) {
				if(arr1[i]==arr2[j]) {
					sum+=arr2[j];
					if(count==0) {
						sum+=arr1[i];
					}
					arr2[j]=0;
					count++;
				}
			}
			arr1[i]=0;
		}
		
		//Displaying the desired outcome:
		System.out.println("\nThe sum of the common elements is: "+sum);
		
		
		
	}
}
