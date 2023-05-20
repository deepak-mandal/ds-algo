package com.cgi;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.Scanner;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 2. Write a Java code to store Sales_Rep details using JDBC API. 
 * [Hint : DriverManager, Connection, PreparedStatement, ResultSet]
 * */
public class StoreSales_Rep {
	public static void main(String[] args) {
		System.out.println("Storing Sales_Rep details using JDBC API: \n");
		
		//Declaring the data type of the data members/attributes
		int rep_id;
		String name, city;
		double commision;
		
		//Taking input from the user to store into the database
		Scanner sc=new Scanner(System.in);
		
		System.out.print("Enter the Rep_ID: ");
		rep_id=sc.nextInt();
		sc.nextLine();
		System.out.print("Enter the Name: ");
		name=sc.nextLine();
		System.out.print("Enter the City: ");
		city=sc.nextLine();
		System.out.print("Enter the Commision: ");
		commision=sc.nextDouble();
		
		try {
			//Specification of JDBC Driver
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//url of the database named "Sales_Management"
			String url="jdbc:mysql://localhost:3306/sales_management"
			+"?verifyServerCertificate=false&useSSL=false&requireSSL=false";
			
			String un="root";		//username
			String pwd="";			//password
			
			String query ="INSERT INTO Sales_Rep values(?, ?, ?, ?)";		//SQL query
			
			
			//Connection Interface
			Connection con=DriverManager.getConnection(url, un, pwd);
			
			//PreparedStatement Interface
			PreparedStatement ps=con.prepareStatement(query);
			ps.setInt(1, rep_id);
			ps.setString(2, name);
			ps.setString(3, city);
			ps.setDouble(4, commision);
			
			int status =ps.executeUpdate();
			System.out.println("Record Inserted Sucessfully");		//displaying the message after successful insertion of data into the database
			
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
