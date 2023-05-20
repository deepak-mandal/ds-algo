package com.dkm;

public class AnonymousInnerClass {
	
	public static void main(String[] args) {
		
		Thread t1 = new Thread(new Runnable(){
			
			@Override
			public void run() {
				System.out.println("Anonymous inner class");
			}
			
		}) ;
		
		t1.start();
		
	}

}
