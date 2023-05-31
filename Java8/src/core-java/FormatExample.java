package javaCollections;

public class FormatExample {

	public static void main(String args[]) {
		
		String name="Raghu";
		int id=1001;
		float salary = 72456.2154f;
		boolean status=true;
		
		System.out.printf("%2$s %3$, .2f %1$d %b",id, name, salary, status);
		
		System.out.printf("\n%d %s %.2f %B", id, name, salary, status);
		
		System.out.printf("\n\nID is %d \n Name is %s. salary is %.2f", id, name, salary);
		
		
		
	}
}
