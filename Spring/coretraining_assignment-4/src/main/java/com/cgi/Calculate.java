package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 1) Create a class Calculate Create a method int addSum(int a, int b);
 *  boolean isEven(int num);*/

public class Calculate {
	
	//declaring addSum() method
	public int addSum(int a, int b) {
		return a+b;
	}
	
	//declaring the isEven() method
	public boolean isEven(int num) {
		boolean result=false;
		//checking for whether the given number is even
		if(num%2==0) {
			result=true;
		}
		return result;
	}

}
