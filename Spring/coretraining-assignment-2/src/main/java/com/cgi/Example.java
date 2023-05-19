package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 1. Write a Lambda Expression to print your company Name.
	Name of the Interface : MyFunction 
	Method Signature      : public String printCompanyName() 
        Name of the Class that contains main method: Example
 * 
 * */

public class Example {
	public static void main(String[] args) {
		
		//Lambda expression to return the company name
		MyFunction mf=() -> {
			return "CGI Information Systems and Management Consultants Pvt. Ltd.";
		};
		
		//Calling the abstract method
		String result=mf.printCompanyName();
		//Displaying the desired result
		System.out.println(result);
		
	}
}
