package com.cgi;

/*
 * 4. Create a Department class to demonstrate the lifecycle of the Spring Bean.
 * */

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DepartmentMain {

	public static void main(String[] args) {
		System.out.println("Department class to demonstrate the lifecycle of the Spring Bean:\n");
		//Using Abstract Application Context Container for lifecycle "ClassPathXmlApplicationContext"

		AbstractApplicationContext ctx = new ClassPathXmlApplicationContext("beaninfo.xml");
		Department dept = (Department)ctx.getBean("dept");
		
		System.out.println("Department Information is: "+dept.getDeptName());
	
		ctx.registerShutdownHook();
		
		
	}
	
}
