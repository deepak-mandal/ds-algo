package com.cgi;

/*
 * 1. Create a Customer class with the following attributes
   custid, custname and Ordervalue. 
   Configure the bean details in the xml file.
   Create a class CustomerMain to implement the DI by Setter method*/

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class CustomerMain {
	public static void main(String[] args) {
	
		
		//Using Application Context Container "ClassPathXmlApplicationContext"
		
		ApplicationContext ctx = new ClassPathXmlApplicationContext("beaninfo.xml");
		Customer customer = (Customer)ctx.getBean("cust");
		
		System.out.println(customer);
		
		
		
	}

}
