package com.cgi.repo;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 2.Create a Repo to do the following
     a) Integer Array of 20 elements.
	 b) Store the states of India as List.
     c) Create a prodList to store list of products.
 * */

import java.util.Arrays;
import java.util.List;
import com.cgi.Product;

public class DataRepo {
	
	//(a). to store 20 elements of int date type in an Array.
	public static int intArr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
	
	//b) to Store the states of India as List.
	public static List<String> states=Arrays.asList("Andaman and Nicobar (UT)", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh (UT)", "Chhattisgarh", "Dadra and Nagar Haveli (UT)", "Daman and Diu (UT)", "Delhi", "Goa", "Gujarat", "Haryana");
	
	//c) Creating a prodList to store list of products.
	public static List<Product> prodList = Arrays.asList(new Product[] {
		new Product(1, "Cell Phone", 2, 520.63),
		new Product(2, "KeyBoard", 20, 7820.88),
		new Product(3, "HeadPhone", 12, 52780.3),
		new Product(4, "Pen", 452, 6920.689),
		new Product(5, "Laptop", 4, 57400.0)
	});
	
	// declaring the getProductByProdId method() to get the Product details for a particular prodId
	public static Product getProductByProdId(int prodId) {
		return prodList.stream().filter(s -> s.getProdId() == prodId).findAny().get();
	}
	
	
}
