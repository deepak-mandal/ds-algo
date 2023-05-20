package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 1. Create a class Product with the following Attributes
      prodId int, prodName String, qty int, price double.
 * */

public class Product {
	//declaring the Data members or attributes as following
	private int prodId;
	private String prodName;
	private int qty;
	private double price;
	
	//constructor with no parameters
	public Product() {
		super();
	}
	
	//constructor with all the attributes
	public Product(int prodId, String prodName, int qty, double price) {
		super();
		this.prodId = prodId;
		this.prodName = prodName;
		this.qty = qty;
		this.price = price;
	}

	//Getter method for prodId
	public int getProdId() {
		return prodId;
	}
	
	//Setter method for prodId
	public void setProdId(int prodId) {
		this.prodId = prodId;
	}

	//getter method for ProdName
	public String getProdName() {
		return prodName;
	}
	
	//setter method for prodName
	public void setProdName(String prodName) {
		this.prodName = prodName;
	}
	
	//getter method for qty attribute
	public int getQty() {
		return qty;
	}
	
	//Setter method for qty attribute
	public void setQty(int qty) {
		this.qty = qty;
	}
	
	//getter method for price
	public double getPrice() {
		return price;
	}

	//setter method for price
	public void setPrice(double price) {
		this.price = price;
	}

	//toString() method for printing the product details
	@Override
	public String toString() {
		return "Product [prodId=" + prodId + ", prodName=" + prodName + ", qty=" + qty + ", price=" + price + "]";
	}
	

}
