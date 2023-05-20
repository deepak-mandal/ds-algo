package com.dkm;

public class ThreadLambdaExp {
	
	public static void main(String[] args) {
		
		Thread t1 = new Thread( () -> System.out.println("thread lambda exp. impl."));
		
		t1.start();
		
	}

}
