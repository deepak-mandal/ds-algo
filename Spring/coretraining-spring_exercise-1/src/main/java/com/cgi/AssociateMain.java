package com.cgi;

/*
 * 3. Create a Associate class with the following attributes          
      associateId, associateName, List<String> roles 
   Configure the bean details in the xml file.
   Create a class AssociateMain to implement the DI and Collections 
   */

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AssociateMain {

	public static void main(String[] args) {
		//Using Application Context Container "ClassPathXmlApplicationContext"

		ApplicationContext ctx = new ClassPathXmlApplicationContext("beaninfo.xml");
		Associate associate = (Associate)ctx.getBean("asc");
		
		System.out.println(associate);
		
		//associate.showData();
				
	}
}
