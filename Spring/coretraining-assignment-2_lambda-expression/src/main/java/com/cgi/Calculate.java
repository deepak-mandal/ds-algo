package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 2. Write a Lambda Expression to pass an integer as Argument and increment the value by Five
	Method Signature :  public int incrementByFive(int a)
	Name of the Class that contains main method: Calculate
*/

public class Calculate {
	public static void main(String[] args) {
		
		//Lambda expression to pass an integer as argument and returning the value by incremented by 5
		CalculateInterface ci = (int a) -> {return a+5;};
		
		//calling the abstract method;
		int result=ci.incrementByFive(10);
		
		//Displaying the desired result
		System.out.println("Value after incremented by five is: "+result);
		
	}
}
