package com.cgi;

/*Write a program to read integer array and find the index of the first
 *  occurance of the largest number. Method should take integer array 
 *  as input and return an integer with the index of the largest number.
 *   Method should return -1 if the array is empty.*/

import java.util.*;

public class Question10 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i;

		System.out.print("Enter the size of array: ");
		int n = sc.nextInt();		//taking length of array
		sc.nextLine();
		//Applying the logic a/c to question
		if (n != 0) {
			//memory allocation for the both array
			int arr[] = new int[n];
			int arr1[] = new int[n];	//taking another (copy) array object
			for (i = 0; i < n; i++) {
				System.out.print("Enter element" + i + " of the array: ");
				arr[i] = sc.nextInt();
				arr1[i] = arr[i];		//just copying each element into arr1

			}
			
			//just sorting the array "arr1"
			Arrays.sort(arr1);
			int max = arr1[n-1];	//to get the maximum element of array

			//Displaying the desired result:-
			for (i = 0; i < n; i++) {
				if (arr[i] == max) {
					System.out.println("The index of the first occurance of the largest number '"+max+"' is: " + i);
					break;
				}
			}
		} else {
			System.out.println(-1);		//Method should return -1 if the array is empty.
		}
		
	}
}
