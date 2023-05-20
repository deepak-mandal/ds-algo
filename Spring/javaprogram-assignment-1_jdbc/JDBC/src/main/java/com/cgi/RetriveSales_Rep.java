package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 1. Write a Java code to retrive Sales_Rep details using JDBC API. 
 * [Hint : DriverManager, Connection, Statement, ResultSet]
 * */

import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class RetriveSales_Rep {
	public static void main(String[] args) {
		System.out.println("Retriving Sales_Rep details using JDBC API: ");
		
		try {
			//Specification of JDBC Driver
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//url to the database named "Sales_Management"
			String url="jdbc:mysql://localhost:3306/sales_management"
			+"?verifyServerCertificate=false&useSSL=false&requireSSL=false";
			
			String un="root";		//username
			String pwd="";			//password
			
			String query ="Select * from Sales_Rep";		//SQL query to retrive data from the table
			
			
			//Connection Interface
			Connection con=DriverManager.getConnection(url, un, pwd);
			
			//Statement Interface
			Statement st=con.createStatement();
			
			//ResultSet Interface
			ResultSet rs=st.executeQuery(query);
			
			while(rs.next()) {
				//Displaying the data in formatted way
				System.out.print(rs.getInt(1)+"	");
				System.out.printf("%20s",rs.getString(2)+"	");
				System.out.printf("%20s",rs.getString(3)+"	");
				System.out.printf("%11s",rs.getDouble(4)+"	");
				System.out.println();		//new Line;
			}
		
		//Exceptions
		}
		catch(ClassNotFoundException cex) {
			System.out.println("Unable to locate the Driver");
		}
		catch(SQLException se) {
			System.out.println("Check the syntax of SQL statement");
		}
		
	}
}
