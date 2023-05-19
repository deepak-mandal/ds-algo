package com.cgi;

/*Write a program to read string array and count the number of vowels in
 *  each string and return  maximum value of vowels present the string.
 *   If string array is empty return -1
 * */

import java.util.*;

public class Question9 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		System.out.println("Enter Sentence: ");
		String sent[]=sc.nextLine().split(" ");		//taking string array as input
		
		//creating the map object to store string and their vowel count in kay-value pair
		Map map=new HashMap();
		
		//iterating through each word of sentence & counting the no of vowel in each string
		for(String x: sent) {
			int count=0;
			for(int i=0; i<x.length(); i++) {
				char ch=x.charAt(i);
				//checking for vowel
				if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') {
					count++;
				}
			}
			map.put(x, count);		//storing string and vowel count in key-value pair
		}
		
		//Displaying the desired output:-
		System.out.println("map: "+map);
		
		if(sent.length==1) {
			System.out.println(-1);
		}
		else { 
			System.out.println(Collections.max(map.values()));
		}
		
		
	}
}
