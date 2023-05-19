package com.cgi;
/*
 * 2. Create a Product class with the following attributes          
      prodcode, prodname, qty, price 
   Configure the bean details in the xml file.
   Create a class CustomerMain to implement the DI using Constructor

 * */
//Dependency injection using constructor
public class Product {
	
	private int prodCode;
	private String prodName;
	private int qty;
	private double price;
	
	public Product() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Product(int prodCode, String prodName, int qty, double price) {
		super();
		this.prodCode = prodCode;
		this.prodName = prodName;
		this.qty = qty;
		this.price = price;
	}

	public int getProdCode() {
		return prodCode;
	}

	public void setProdCode(int prodCode) {
		this.prodCode = prodCode;
	}

	public String getProdName() {
		return prodName;
	}

	public void setProdName(String prodName) {
		this.prodName = prodName;
	}

	public int getQty() {
		return qty;
	}

	public void setQty(int qty) {
		this.qty = qty;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	@Override
	public String toString() {
		return "Product [prodCode=" + prodCode + ", prodName=" + prodName + ", qty=" + qty + ", price=" + price + "]";
	}
	
	

	
	
}
