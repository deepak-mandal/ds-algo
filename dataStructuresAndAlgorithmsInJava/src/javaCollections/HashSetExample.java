package javaCollections;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class HashSetExample {
	
	public static void main(String[] args) {
		
		Set<String> nameSet = new HashSet<>();
		
		nameSet.add("deepak");
		nameSet.add("rosy");
		nameSet.add("tina");
		nameSet.add("iitg");
		
		System.out.println(nameSet);
		
		
		for(Object o: nameSet) {
			System.out.println(o);
		}
		
		System.out.println();
		Iterator<String> it = nameSet.iterator();
		
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
	}

}
