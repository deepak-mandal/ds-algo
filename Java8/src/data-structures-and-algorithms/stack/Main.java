package dataStructuresAndAlgorithmsInJava.stack;

public class Main {

	public static void main(String[] args) throws StackUnderflowException {
		Stack<String> stack = new Stack<>();
		
		stack.push("Java");
		System.out.println("\nSize (after adding Java): "+stack.size());
		System.out.println("\nContents (after adding Java): "+stack);
		
		stack.push("Python");
		stack.push("Golang");
		stack.push("JavaScript");
		
		System.out.println("\nSize (after adding multiple elements) : "+stack.size());
		System.out.println("\nContents (after adding multiple elements): "+stack);
		
		stack.pop();
		System.out.println("\nStack contents (after popping element): "+stack);
		
		stack.push("C++");
		System.out.println("\nStack contents: "+stack);
		
		System.out.println("\nPeek at last added element: "+stack.peek());
		System.out.println("Stack contents(after peek): "+stack);
		System.out.println("Stack size (after peek): "+stack.size());
		
		System.out.println("\n pop last added element: "+stack.pop());
		System.out.println("Stack content (after pop): "+ stack);
		System.out.println("Stack size (after pop): "+stack.size());
		
		
		System.out.println("\nPeek after pop: "+stack.peek());
		
		stack.pop();
		stack.pop();
		stack.pop();
//		stack.pop();
		
	}
	
}
