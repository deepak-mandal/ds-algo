package dataStructuresAndAlgorithmsInJava.stack;

public class Stack<T> {
	
	private Element<T> top;
	private int size = 0;
	
	public Stack() {
		
	}
	
	public boolean isEmpty() {
		return size==0;
	}
	
	public boolean isFull() {
		return false;
	}
	
	public int size() {
		return size;
	}
	
	@Override
	public String toString() {
		if(top==null) {
			return "";
		}
		return top.toString();
	}
	
	
	//O(1) time complexity
	public void push(T data) {
		Element<T> node = new Element<T>(data);
		if(top!=null) {
			node.setNext(top);
		}
		top = node;
		size++;
	}
	
	//O(1) time complexity
	public T pop() throws StackUnderflowException{
		if(top==null) {
			throw new StackUnderflowException("Stack empty, cannot pop element");
		}
		
		T data = top.getData();
		top=top.getNext();
		size--;
		return data;
	}
	
	public T peek() throws StackUnderflowException{
		if(top==null) {
			throw new StackUnderflowException("Stack empty, cannot pop element");
		}
		return top.getData();
		
	}

}
