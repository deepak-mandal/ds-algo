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

public class School {
	
	private String schoolName;
	private String location;
	
	public School() {
		super();
		// TODO Auto-generated constructor stub
	}

	public School(String schoolName, String location) {
		super();
		this.schoolName = schoolName;
		this.location = location;
	}

	public String getSchoolName() {
		return schoolName;
	}

	public void setSchoolName(String schoolName) {
		this.schoolName = schoolName;
	}

	public String getLocation() {
		return location;
	}

	public void setLocation(String location) {
		this.location = location;
	}

	@Override
	public String toString() {
		return "School [schoolName=" + schoolName + ", location=" + location + "]";
	}
	
	

}
