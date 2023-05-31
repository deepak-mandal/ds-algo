package javaCollections;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ArrayListExample {

	public static void main(String[] args) {
		List <String> nameList = new ArrayList<>();
		nameList.add("Tina");
		nameList.add("Rosy");
		nameList.add("John");
		nameList.add("Pooja");
		nameList.add("John");
		nameList.add("Rosy");
		
		System.out.println(nameList);
		nameList.add(5, "George");
		System.out.println(nameList);
		
		
		for(int i=0; i<nameList.size(); i++) {
			System.out.println(nameList.get(i));
		}
		
		for(Object o: nameList) {
			System.out.println(o);
		}
		
		Iterator<String> it= nameList.iterator();
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
	}
}
