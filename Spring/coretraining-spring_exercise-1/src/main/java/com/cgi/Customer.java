package com.cgi;

/*
 * 1. Create a Customer class with the following attributes
   custid, custname and Ordervalue. 
   Configure the bean details in the xml file.
   Create a class CustomerMain to implement the DI by Setter method*/

public class Customer {

	private int custId;
	private String custName;
	private double orderValue;
	
	public Customer() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Customer(int custId, String custName, double orderValue) {
		super();
		this.custId = custId;
		this.custName = custName;
		this.orderValue = orderValue;
	}

	public int getCustId() {
		return custId;
	}

	public void setCustId(int custId) {
		this.custId = custId;
	}

	public String getCustName() {
		return custName;
	}

	public void setCustName(String custName) {
		this.custName = custName;
	}

	public double getOrderValue() {
		return orderValue;
	}

	public void setOrderValue(double orderValue) {
		this.orderValue = orderValue;
	}

	@Override
	public String toString() {
		return "Customer [custId=" + custId + ", custName=" + custName + ", orderValue=" + orderValue + "]";
	}
	
	
	
	
	
	
}
