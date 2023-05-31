package com.dkm;
public class Student {
    private int id;

    private String name;
    
    private int age;
    
	public Student() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	public Student(int id, String name, int age) {
		super();
		this.id = id;
		this.name = name;
		this.age = age;
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	@Override
	public String toString() {
		return "Student [id=" + id + ", age=" + age + ", name=" + name + "]";
	}

    //getter, setter,constructor, toString
    
    

    


}
