package com.cgi.Model;

/*
1. Create a Model class Student with the following attributes (5 Marks)
int rollno, String name, int marks, double grade
*/

public class Student {
	private int rollno;
	private String name;
	private int marks;
	private double grade;
	
	//Constructor with no parameter
	public Student() {
		super();
	}

	//Constructor with all parameter
	public Student(int rollno, String name, int marks, double grade) {
		super();
		this.rollno = rollno;
		this.name = name;
		this.marks = marks;
		this.grade = grade;
	}

	//getter method for rollno attribute
	public int getRollno() {
		return rollno;
	}

	//setter method for rollno
	public void setRollno(int rollno) {
		this.rollno = rollno;
	}

	//getter and setter method() for name
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	//getter & setter method for marks data member
	public int getMarks() {
		return marks;
	}

	public void setMarks(int marks) {
		this.marks = marks;
	}

	//getter method for grade
	public double getGrade() {
		return grade;
	}

	//setter method for grade 
	public void setGrade(double grade) {
		this.grade = grade;
	}

	//toString() method for printing
	@Override
	public String toString() {
		return "Student [rollno=" + rollno + ", name=" + name + ", marks=" + marks + ", grade=" + grade + "]";
	}
	
	

}
