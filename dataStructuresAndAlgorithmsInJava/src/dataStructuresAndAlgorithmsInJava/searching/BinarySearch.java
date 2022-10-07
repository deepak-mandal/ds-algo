package dataStructuresAndAlgorithmsInJava.searching;

public class BinarySearch {

	public static int binarySearch(String[] list, String element) {

		System.out.println("\nSearching.. " + element + ": ");

		int low = 0;
		int high = list.length - 1;

		while (low <= high) {
			int mid = (low + high) / 2;

			System.out.println("low: " + low + " High: " + high + " Mid: " + mid + " Mid element: " + list[mid]);

			if (list[mid].equals(element)) {
				return mid;
			} else if (list[mid].compareTo(element) < 0) {
				low = mid + 1;
			} else {
				high = mid - 1;

			}
		}
		return -1;
	}

	public static void main(String[] args) {
		String sortedList[] = new String[] { "Alex", "Ben", "Carl", "Dora", "Elise", "Fiona", "Gerald", "Harry",
				"Irene", "Jeff", "Kris", "Lewis", "Marry", "Nora", "Ophelia", "Peter" };

		System.out.println("\nElement index: " + binarySearch(sortedList, "Harry"));
	}
}
