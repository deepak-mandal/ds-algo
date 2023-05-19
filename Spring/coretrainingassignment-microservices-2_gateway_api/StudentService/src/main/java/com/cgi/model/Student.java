package com.cgi.model;
/*Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * Create a following services

   1. Gateway API --- 8080
   2. SchoolService -------8081
   3. StudentService-------8082

Client Request must be accessed from the Gateway API 

 * */
//creating Student model class
public class Student {
	
	private int rollno;
	private String name;
	private String department;
	private double fee;
	
	public Student() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Student(int rollno, String name, String department, double fee) {
		super();
		this.rollno = rollno;
		this.name = name;
		this.department = department;
		this.fee = fee;
	}

	public int getRollno() {
		return rollno;
	}

	public void setRollno(int rollno) {
		this.rollno = rollno;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getDepartment() {
		return department;
	}

	public void setDepartment(String department) {
		this.department = department;
	}

	public double getFee() {
		return fee;
	}

	public void setFee(double fee) {
		this.fee = fee;
	}

	
	
	
	
	
	

}
