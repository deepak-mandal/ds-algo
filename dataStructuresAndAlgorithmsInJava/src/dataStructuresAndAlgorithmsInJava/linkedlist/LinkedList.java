package dataStructuresAndAlgorithmsInJava.linkedlist;

public class LinkedList<T extends Comparable<T>> {

	private Node<T> head;

	public LinkedList() {

	}

	public void insertAtHead(T data) {
		Node<T> node = new Node<T>(data);

		if (head != null) {
			node.setNext(head);
		}
		head = node;
	}

	@Override
	public String toString() {
		if (head == null) {
			return "";
		}
		return head.toString();
	}

	public int countNodes() {
		Node<T> curr = head;
		int count = 0;
		while (curr != null) {
			curr = curr.getNext();
			count++;
		}
		return count;
	}

	public void insertAtTail(T data) {
		Node<T> node = new Node<T>(data);
		if (head == null) {
			head = node;
			return;
		}
		Node<T> curr = head;
		while (curr.getNext() != null) {
			curr = curr.getNext();
		}
		curr.setNext(node);
	}

	public void insert(T data, int index) {
		if (index <= 0) {
			insertAtHead(data);
			return;
		}

		Node<T> curr = head;
		int currIndex = 1;

		while (curr.getNext() != null && currIndex < index) {
			curr = curr.getNext();
			currIndex++;
		}
		Node<T> next = curr.getNext();
		Node<T> newNode = new Node<T>(data);
		newNode.setNext(next);
		curr.setNext(newNode);
	}

	public T pop() {
		if (head == null) {
			return null;
		}

		Node<T> first = head;

		head = head.getNext();
		return first.getData();

	}

	public boolean contains(T data) {
		Node<T> curr = head;
		while (curr != null) {
			if (curr.getData().equals(data)) {
				return true;
			}
			curr = curr.getNext();
		}
		return false;
	}

	public void delete(T data) {
		Node<T> curr = head;
		Node<T> prev = null;

		while (curr != null) {
			if (curr.getData().equals(data)) {
				if (prev == null) {
					head = head.getNext();
				} else {
					prev.setNext(curr.getNext());
				}
				break;
			}
			prev = curr;
			curr = curr.getNext();
		}
	}

}
