package com.cgi;
/*
 * 2. Create a Product class with the following attributes          
      prodcode, prodname, qty, price 
   Configure the bean details in the xml file.
   Create a class CustomerMain to implement the DI using Constructor

 * */
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class ProductMain {

	public static void main(String[] args) {
		//Using Application Context Container "ClassPathXmlApplicationContext"
	
		ApplicationContext ctx = new ClassPathXmlApplicationContext("beaninfo.xml");
		Product product = (Product)ctx.getBean("prod");
		
		System.out.println(product);
				
	}
}
