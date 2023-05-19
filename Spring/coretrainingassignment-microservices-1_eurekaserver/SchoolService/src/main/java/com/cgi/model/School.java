package com.cgi.model;

public class School {
	
	private int registrationId;
	private String schoolName;
	private String location;
	
	public School() {
		super();
		// TODO Auto-generated constructor stub
	}

	public School(int registrationId, String schoolName, String location) {
		super();
		this.registrationId = registrationId;
		this.schoolName = schoolName;
		this.location = location;
	}

	public int getRegistrationId() {
		return registrationId;
	}

	public void setRegistrationId(int registrationId) {
		this.registrationId = registrationId;
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
		return "School [registrationId=" + registrationId + ", schoolName=" + schoolName + ", location=" + location
				+ "]";
	}
	
	

}
