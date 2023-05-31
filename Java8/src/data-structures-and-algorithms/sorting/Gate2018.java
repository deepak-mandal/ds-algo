package dataStructuresAndAlgorithmsInJava.sorting;

public class Gate2018 {
	
	public static void fun(int z) {
		System.out.print(z%10);
		if((z/10)!=0){
			fun(z/10);
		}
		System.out.print(z%10);
	}
	
	public static void main(String[] args) {
		fun(4321);
	}

}

