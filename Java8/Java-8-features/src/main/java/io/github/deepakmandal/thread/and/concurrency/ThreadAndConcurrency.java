package io.github.deepakmandal.thread.and.concurrency;

public class ThreadAndConcurrency implements Runnable {
	
	@Override
	public void run(){
		for(int i=0; i<5; i++) {
			try {
				Thread.sleep(3000);
			}catch(Exception e) {
				e.printStackTrace();
			}
			String threadName = Thread.currentThread().getName();
			System.out.println(threadName+": "+i);
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread thread1 = new Thread(new ThreadAndConcurrency(), "thread1");
		Thread thread2 = new Thread(new ThreadAndConcurrency());
		thread2.setName("thread2");
		
		thread1.start();
		thread2.start();

	}

}
