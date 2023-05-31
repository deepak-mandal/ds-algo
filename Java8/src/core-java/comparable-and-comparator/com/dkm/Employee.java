package com.dkm;

public class Employee  implements Comparable<Employee> {

    private int id;
    private String name;
    private int age;


    //getter,setter,constructor

    public int compareTo(Employee obj){

        if(this.id==obj.id){
            return 0;
        }else if(this.id>obj.id){
            return 1;
        }else{
            return -1;
    }


    }
    
    


	public Employee(int id, String name, int age) {
		super();
		this.id = id;
		this.name = name;
		this.age = age;
	}




	public Employee() {
		super();
		// TODO Auto-generated constructor stub
	}




	@Override
	public String toString() {
		return "Employee [id=" + id + ", name=" + name + ", age=" + age + "]";
	}


	public int getId() {
		return id;
	}


	public void setId(int id) {
		this.id = id;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public int getAge() {
		return age;
	}


	public void setAge(int age) {
		this.age = age;
	}
	
	
}
