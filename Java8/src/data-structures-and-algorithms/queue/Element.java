package dataStructuresAndAlgorithmsInJava.queue;

public class Element<T> {

	private T data;
	private Element<T> next;
	private Element<T> previous;

	public Element(T data) {
		this.data = data;
		setNext(null);
	}

	public Element<T> getNext() {
		return next;
	}

	public void setNext(Element<T> next) {
		this.next = next;
	}

	public Element<T> getPrevious() {
		return previous;
	}

	public void setPrevious(Element<T> previous) {
		this.previous = previous;
	}

	public T getData() {
		return data;
	}

	@Override
	public String toString() {
		return String.valueOf(data) + "<->" + ((next == null) ? "|" : next.toString());
	}

}
