package javaCollections;

import java.util.Set;
import java.util.TreeSet;

public class TreeSetEx {
	
	public static void main(String[] args) {
		
		Set<Object> nameSet = new TreeSet<>();  //Object could be any thing even user defined model like Employee 
		
		nameSet.add("tina");
		nameSet.add("rosni");
		nameSet.add("pooja");
		
		System.out.println(nameSet);
		
		for(Object o: nameSet) {
			System.out.println(o);
		}
		
		
		
		
		
		
		
	}

}
