package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * Hibernate Exercise -3

Create a Model class Mentor with the following Attribute and Insert record
    id, name, tech
 * */

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class MentorInsert {

	public static void main(String[] args) {
		
		//creating configuration object
		Configuration cfg=new Configuration();
		//populates the data of the configuration file
		cfg.configure("hibernate.cfg.xml");	
		
		//creating session factory object
		SessionFactory factory=cfg.buildSessionFactory();
		
		//Creating session object
		Session session=factory.openSession();
		
		//creating transaction object
		Transaction tran=session.beginTransaction();
		
		//Create an object for Mentor
		Mentor asso=new Mentor();
		asso.setId(1402);
		asso.setName("Deepak Kumar");
		asso.setTech("Java Full-stack with Angular as front-end, Spring as backend");
		
		session.persist(asso);
		tran.commit();
		session.close();
		System.out.println("Mentor Data Inserted successfully");
		
	}
}
