package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * Hibernate Exercise -3
 * 
 
 ORM tools -> (Hibernate Framework)
 Object Relational Mapping
 Usage of ORM is to create incompatible Data types


 Java Object 
 ------------
 Employee e = new Employee();
 e -> object

 Employee:-
 empId -> int
 ename -> string
 salary -> int


 Database
 ---------
 Employee:-
 empId -> int
 ename -> varchar
 salary -> int

 * to relate java datatype into database data type ; we need object relation mapping 
 * => for this we will use Hibernate Framework


 

Create a Model class Mentor with the following Attribute and Insert record
    id, name, tech
 * */

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="mentor")
public class Mentor {

	@Id
	private int id;
	private String name;
	private String tech;
	
	public Mentor() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Mentor(int id, String name, String tech) {
		super();
		this.id = id;
		this.name = name;
		this.tech = tech;
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

	public String getTech() {
		return tech;
	}

	public void setTech(String tech) {
		this.tech = tech;
	}

	
}
