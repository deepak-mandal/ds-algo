package javaCollections;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapExample {

	public static void main(String args[]) {
		Map map = new HashMap();
		
		map.put("first", "1st");
		map.put("2nd", new Float(2.0f));
		map.put("third", "3rd");
		map.put("third", "III");
		
		//to view the map
		//return the set view of keys
		
		Set set = map.keySet();
		
		//return collection view of values
		Collection collection = map.values();
		
		//returns set view of key value mappings
		Set mapSet = map.entrySet();
		System.out.println("Set: "+ set + "\n" + "collection: " + mapSet);
		
		
	}
}
