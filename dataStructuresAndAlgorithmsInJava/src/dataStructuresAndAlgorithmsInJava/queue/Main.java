package dataStructuresAndAlgorithmsInJava.queue;

public class Main {

	public static void main(String[] args) throws QueueUnderflowException {
		
	Queue<String> queue = new Queue<>();

	queue.enqueue("Alice");
	System.out.println("Is empty: "+queue.isEmpty());
	System.out.println("Is full: "+queue.isFull());
	System.out.println("Size: "+queue.size());
	System.out.println("\nContents: "+queue);
	queue.enqueue("Brett");
	queue.enqueue("Cheryl");
	queue.enqueue("Dan");
	queue.enqueue("Elise");
	System.out.println("\nSize(added 5 elements): "+queue.size());
    System.out.println("\nContents: "+queue);
    
    System.out.println("\nDequeue1: "+queue.dequeue());
    System.out.println("\nCOntents: "+queue);
    System.out.println("\nPeek at first element: "+queue.peek());
    System.out.println("Queue contents (after peek): "+queue);
    System.out.println("Queue size (after peek): "+queue.size());
    System.out.println(queue.dequeue());
    System.out.println(queue.dequeue());
    System.out.println(queue.dequeue());
    System.out.println("Queue contents (after dequeue): "+queue);
    System.out.println("Queue size(after dequeue): "+queue.size());
    System.out.println("\nPeek after dequeue: "+queue.peek());
    
	}
}
