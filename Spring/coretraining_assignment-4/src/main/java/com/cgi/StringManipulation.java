package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 2) Create a class StringManipulation and create a method 
 * int vowelCount(String name); int characterCount(String str);*/

public class StringManipulation {
	
	//Declaring vowelCount() method
	public int vowelCount(String name) {
		int vowelCount = 0;		//to store the no of count of vowel
		for (int i = 0; i < name.length(); i++) {		//iterating through each character of string
			char c = name.toLowerCase().charAt(i);
			// checking for vowels
			if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
				vowelCount++;
			}
		}
		//returning the desired output
		return vowelCount;
	}
	
	//Declaring characterCount() method
	public int characterCount(String str) {
		char charCount = 0;			//to store the no of count of character
		for (int i = 0; i < str.length(); i++) {		//iterating through each character of string
			char c = str.toLowerCase().charAt(i); 		// converting the char data type

			// checking for Character
			if (Character.isLetter(c)) {
				charCount++;
			}
		}
		return charCount;			//returning the desired result
	}

}
