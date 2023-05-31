package dataStructuresAndAlgorithmsInJava.searching;

public class LinearSearch {

	public static int linearSearch(String[] list, String element) {
		System.out.println("\n Searching..." + element + ": ");
		for (int i = 0; i < list.length; i++) {
			System.out.println(i + " ");
			if (list[i].equals(element)) {
				return i;
			}
		}
		return -1;
	}

	public static void main(String[] args) {
		String unSortedList[] = new String[] { "Alex", "Dora", "Carl", "Ben", "Ophelia", "Elise", "Fiona", "Gerald",
				"Harry", "Peter", "Irene", "Jeff", "Kris", "Lewis", "Mary", "Nora" };

		System.out.println("\n Element index: " + linearSearch(unSortedList, "Harry"));

	}

}
