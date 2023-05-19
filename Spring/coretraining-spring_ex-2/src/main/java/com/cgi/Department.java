package com.cgi;

/*4. Create a Department class to demonstrate the lifecycle of the Spring Bean.*/

import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;

public class Department implements InitializingBean, DisposableBean {

	private String deptName;

	public String getDeptName() {
		return deptName;
	}

	public void setDeptName(String deptName) {
		this.deptName = deptName;
	}

	public Department() {
		System.out.println("Constructor of Department Class is Called");
	}

	@Override
	public void destroy() throws Exception {
		System.out.println("Bean which is loaded is cleaned up!");

	}

	@Override
	public void afterPropertiesSet() throws Exception {
		System.out.println("Value for the attributes is Assigned");

	}

}
