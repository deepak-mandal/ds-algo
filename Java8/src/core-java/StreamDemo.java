package javaCollections;

import java.util.HashMap;
import java.util.Map;

class Customer {

	
	int id;
	String name;
	public int getId() {
		return id;
	}
	
	public void setId(int id) {
		this.id=id;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name=name;
	}
	
	public Customer(int id, String name) {
		super();
		this.id=id;
		this.name=name;
	}
	
	
}

public class StreamDemo{
	public static void main(String[] args) {
		Map<Integer, Customer> map = new HashMap<>();
		
		map.put(1, new Customer(1, "deepak"));
		map.put(2, new Customer(34, "roshni"));
		map.put(3, new Customer(36, "mayuri"));
		map.put(4, new Customer(93, "seema"));
		map.put(5, new Customer(100, "kumar"));
		
		map.forEach((k, v) -> System.out.println("Key: "+k+" value: "+v.getName()));
	}
}