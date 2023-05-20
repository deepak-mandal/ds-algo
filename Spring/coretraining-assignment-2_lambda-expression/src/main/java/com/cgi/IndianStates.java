package com.cgi;
/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 4. Write a Lambda Expression to store Names of the states in India
 *  in an ArrayList. 
	Print them using For Each Loop.
 * 
 * */

import java.util.Arrays;
import java.util.List;

public class IndianStates {
	public static void main(String[] args) {
		
		//Creating List object to store the names of states in India
		List <String> states = Arrays.asList("Andaman and Nicobar (UT)", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh (UT)", "Chhattisgarh", "Dadra and Nagar Haveli (UT)", "Daman and Diu (UT)", "Delhi", "Goa", "Gujarat", "Haryana");
		
		//Lambda expression to display the desired result:
		states.forEach((statesName) -> System.out.println(statesName));
		
	}
}
