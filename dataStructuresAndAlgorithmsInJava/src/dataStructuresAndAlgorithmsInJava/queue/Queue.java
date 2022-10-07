package dataStructuresAndAlgorithmsInJava.queue;

public class Queue<T> {

	private Element<T> front;
	private Element<T> rear;

	private int size = 0;

	public Queue() {

	}

	public boolean isEmpty() {
		return size == 0;
	}

	public boolean isFull() {
		return false;
	}

	public int size() {
		return size;
	}

	@Override
	public String toString() {
		if (front == null) {
			return "";
		}
		return front.toString();
	}

	public void enqueue(T data) {
		Element<T> element = new Element<>(data);

		size++;

		if (front == null) {
			front = element;
			rear = element;
			return;
		}

		rear.setNext(element);
		element.setPrevious(rear);
		rear = element;
	}

	public T dequeue() throws QueueUnderflowException {

		if (front == null) {
			throw new QueueUnderflowException("Empty queue, cannot dequeue element");
		}

		T data = front.getData();
		if (front == rear) {
			front = null;
			rear = null;
		} else {
			front = front.getNext();
			front.setPrevious(null);
		}
		size--;
		return data;

	}

	public T peek() throws QueueUnderflowException {
		if (front == null) {
			throw new QueueUnderflowException("Empty queue, cannot dequeue element");
		}
		return front.getData();
	}

}
