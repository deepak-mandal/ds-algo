package dataStructuresAndAlgorithmsInJava.linkedlist;

import java.time.Duration;
import java.time.Instant;

public class TimeComplexityCalculation {

	private static void insert100000ElementsAtHead(LinkedList<Integer> list) {
		for (int i = 0; i < 100000; i++) {
			list.insertAtHead(i);
		}
	}

	private static void insert100000ElementsAtTail(LinkedList<Integer> list) {
		for (int i = 0; i < 100000; i++) {
			list.insertAtTail(i);
		}
	}

	public static void main(String[] args) {
		LinkedList<Integer> linkedList1 = new LinkedList<>();

		Instant start = Instant.now();
		insert100000ElementsAtHead(linkedList1);
		Instant end = Instant.now();
		System.out.println("\nTIme taken to insert 100000 elements at head : " + Duration.between(start, end));

		LinkedList<Integer> linkedList2 = new LinkedList<>();

		start = Instant.now();
		insert100000ElementsAtTail(linkedList2);
		end = Instant.now();
		System.out.println("\nTime taken to insert 100000 elements at Tail: " + Duration.between(start, end));

	}

}
