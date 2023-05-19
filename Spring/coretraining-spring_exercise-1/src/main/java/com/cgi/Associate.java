package com.cgi;


/*
 * 3. Create a Associate class with the following attributes          
      associateId, associateName, List<String> roles 
   Configure the bean details in the xml file.
   Create a class AssociateMain to implement the DI and Collections 
   */


import java.util.Iterator;
import java.util.List;

public class Associate {
	
	private int associateId;
	private String associateName;
	private List<String> roles;

	public Associate() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Associate(int associateId, String associateName, List<String> roles) {
		super();
		this.associateId = associateId;
		this.associateName = associateName;
		this.roles = roles;
	}

	public int getAssociateId() {
		return associateId;
	}

	public void setAssociateId(int associateId) {
		this.associateId = associateId;
	}

	public String getAssociateName() {
		return associateName;
	}

	public void setAssociateName(String associateName) {
		this.associateName = associateName;
	}

	public List<String> getRoles() {
		return roles;
	}

	public void setRoles(List<String> roles) {
		this.roles = roles;
	}

	public void showData() {
		System.out.println("Associate ID is: "+associateId);
		System.out.println("Associate Namre is: "+associateName);
		System.out.println("Modules are: ");
		
		Iterator itr = roles.iterator();
		while(itr.hasNext()) {
			System.out.println(itr.next());
		}
	}

	@Override
	public String toString() {
		return "Associate [associateId=" + associateId + ", associateName=" + associateName + ", roles=" + roles + "]";
	}
	
	
	
	

}
