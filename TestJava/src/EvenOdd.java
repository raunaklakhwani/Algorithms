
class Mythread1 extends Thread {
	public static Integer i = 1;

	int k;

	public Mythread1(int k) {
		this.k = k;
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		super.run();
		while (true) {
			try {
				//System.out.println(i);
				//System.out.println(this.getState());
				synchronized (i) {
					if (i <= 100) {
						if ((i & 1) == k) {
							System.out.println(i);
							i += 1;
							i.notify();
						} else {
							i.wait();
						}
					} else{
						break;
					}
				}

			} catch (Exception e) {

			}
		}
	}

	public synchronized void print() {

	}

}

public class EvenOdd {

	public static void main(String[] args) {
		System.out.println("Ronak");
		Mythread1 even = new Mythread1(0);
		Mythread1 odd = new Mythread1(1);
		odd.start();
		even.start();

		System.out.println("End");
	}

}
