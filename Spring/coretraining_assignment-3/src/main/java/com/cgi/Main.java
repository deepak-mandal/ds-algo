package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 3. Create a Main Class to do the following operations

       a) Extract Array elements which are divisible by 4
	   b) Extract the Names of the state that ends with "a".
	   c) Print all the product info
	   
	   d) Print the Product that has the highest price
	   e) Print the Product that has the lowest price
	   
	   f) Print the Product details for a particular prodId
 * */

import java.util.Arrays;
import java.util.DoubleSummaryStatistics;
import com.cgi.repo.DataRepo;

public class Main {
	public static void main(String args[]) {

		// a) Extract Array elements which are divisible by 4
		Arrays.stream(DataRepo.intArr).filter(m -> m % 4 == 0).sorted().forEach(s -> System.out.print(s + " "));
		System.out.println("\n");

		// b) Extract the Names of the state that ends with "a".
		DataRepo.states.stream()
		.filter(n -> n.endsWith("a"))
		.sorted()
		.forEach(s1 -> System.out.println(s1 + " "));

		System.out.println();
		
		//c) Print all the product info
		DataRepo.prodList.stream()
		.forEach(em -> System.out.println(em));
				
		System.out.println();
		
		//d) Print the Product that has the highest price
		DoubleSummaryStatistics stats = DataRepo.prodList.stream()
				.mapToDouble(e -> e.getPrice())
				.summaryStatistics();
		
		System.out.println("Highest Price is "+stats.getMax());
		
		//e) Print the Product that has the lowest price
		System.out.println("Lowest Price is "+stats.getMin());
		System.out.println();
		
		//f) Print the Product details for a particular prodId
		System.out.println(DataRepo.getProductByProdId(1));
				
		
		

	}
}
