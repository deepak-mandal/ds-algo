package dataStructuresAndAlgorithmsInJava.linkedlist;

public class Main {

	public static void main(String[] args) {

		Node<Integer> intNode1 = new Node<>(100);
		System.out.println("Integer node1: " + intNode1);

		Node<String> stringNode1 = new Node<>("Java");

		System.out.println("String node1: " + stringNode1);

		Node<Integer> intNode2 = new Node<>(200);
		Node<String> stringNode2 = new Node<>("Python");

		intNode1.setNext(intNode2);
		stringNode1.setNext(stringNode2);

		System.out.println("\nInteger node1 (two linked list nodes): " + intNode1);
		System.out.println("\nString node1 (two linked nodes): " + stringNode1);

		Node<Integer> intNode3 = new Node<>(300);
		Node<String> stringNode3 = new Node("JavaScript");

		intNode2.setNext(intNode3);
		stringNode2.setNext(stringNode3);

		System.out.println("\nInteger node1 (three linked nodes): " + intNode1);
		System.out.println("\nString node1 (three linked nodes): " + stringNode1);

		// Linked list implementation
		LinkedList<Integer> linkedList = new LinkedList<>();

		System.out.println("Linked list node count(empty): " + linkedList.countNodes());

		linkedList.insertAtTail(100);
		System.out.println("\nLinked list node count(1 node): " + linkedList.countNodes());

		System.out.println(linkedList);
		linkedList.insertAtHead(200);

		System.out.println("linked list (2 nodes): " + linkedList);

		linkedList.insertAtHead(300);
		linkedList.insertAtHead(400);
		linkedList.insertAtHead(500);

		System.out.println("Linked list (5 nodes): " + linkedList);

		System.out.println("\nLinked list node count: " + linkedList.countNodes());
		System.out.println(linkedList);

		linkedList.insertAtTail(200);
		System.out.println("\n linked list node count(2 node): " + linkedList.countNodes());

		System.out.println(linkedList);
		linkedList.insertAtTail(300);
		linkedList.insertAtTail(400);
		linkedList.insertAtTail(500);
		linkedList.insertAtTail(600);
		linkedList.insertAtHead(5000);

		System.out.println("\nLinked list node count : " + linkedList.countNodes());
		System.out.println(linkedList);

		// Insert at index
		System.out.println("INSERT AT INDEX");
		linkedList.insert(100, 0);
		System.out.println(linkedList);
		linkedList.insert(99, -1);
		System.out.println(linkedList);
		linkedList.insert(400, 5);
		System.out.println(linkedList);
		linkedList.insert(300, 10);
		System.out.println(linkedList);
		linkedList.insertAtTail(100);
		linkedList.insertAtTail(101);
		linkedList.insertAtTail(102);
		linkedList.insertAtTail(103);
		System.out.println(linkedList);
		System.out.println();
		linkedList.insert(500, 5);
		System.out.println(linkedList);

		linkedList.insertAtTail(100);
		linkedList.insertAtTail(101);
		linkedList.insertAtTail(104);
		System.out.println(linkedList);
		System.out.println();
		System.out.println(linkedList.pop());
		System.out.println(linkedList);

		System.out.println("\nList contains 101? " + linkedList.contains(101));
		System.out.println("\n list contains 10000? " + linkedList.contains(1000));

		System.out.println(linkedList);
		linkedList.delete(102);
		System.out.println(linkedList);
		linkedList.delete(100);
		System.out.println(linkedList);
		linkedList.delete(200);
		System.out.println(linkedList);

	}

}
