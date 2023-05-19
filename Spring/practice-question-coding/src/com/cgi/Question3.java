package com.cgi;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*Write a Java code to find the max vowel string in a sentence.
 * 
 * */

public class Question3 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		System.out.println("Enter Sentence: ");
		String sent[]=sc.nextLine().split(" ");		//taking string as input
		
		//creating the map object to store in key value pair form of "string" : "vowel count"
		Map map=new HashMap();		
		//iterating through each string element of array.
		for(String x: sent) {
			int count=0;
			for(int i=0; i<x.length(); i++) {
				char ch=x.charAt(i);
				if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') {
					count++;		//counting vowel in each string
				}
			}
			map.put(x, count);		//then storing "string" : "their count"
		}
		
		//Printing the desired result:-
		System.out.println("'String' & 'no of Occurrence' pair is given as:\n"+map);
		
		for(Object x: map.keySet()) {
			if(map.get(x)==Collections.max(map.values())) {
				System.out.println("The max vowel string in a sentence: "+x);
			}
		}	
		
	
	}
}
