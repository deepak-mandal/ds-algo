package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 3. Write a Lambda Expression to pass 2 strings as Arguments and concatenate them.
	Name of the Interface : StringConcat 
	Method Signature : public String joinString (String a, String b) 
	Name of the Class that contains main method: ModifyString
 * */

public class ModifyString {
	public static void main(String[] args) {
		//Lambda expression to pass 2 string as argument and returning by concatenating them 
		StringConcat sc = (a, b) -> {return a+b;};
		
		//call the abstract method 
		String result=sc.joinString("Lambda", "Expression");
		
		//printing the desired result
		System.out.println(result);
	}
}
