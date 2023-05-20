package com.dkm;

//Thread is a concurrent light weight process (clone the CPU)
//thread hs 3 part => virtual CPU + code (runnable interface) + data(could be optional)


class StepsToPerform implements Runnable{
	
	@Override
	public void run() {
		System.out.println("Thread is running..");
	}
	
}


public class ThreadDemo {

	public static void main(String[] args) {
		
		StepsToPerform sp = new StepsToPerform();
		Thread t1 = new Thread(sp);
		t1.start();
	}
	
	
	
}
