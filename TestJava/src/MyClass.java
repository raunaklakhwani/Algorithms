
class MyThread2 extends Thread {
	static Integer i = 0;

	int j;
	int k;
	int l;

	public MyThread2(int j, int k, int l) {
		this.j = j;
		this.k = k;
		this.l = l;
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		super.run();

		while (true) {

			print();

		}

	}

	public synchronized void print() {
		try {
			if (i == j || i == l) {
				System.out.println(k);
				i = (i + 1) % 4;
				i.notify();
			} else {
				i.wait();
			}
			// i.notify();
		} catch (Exception e) {

		}
	}
}

public class MyClass {

	public static void main(String[] args) {
		MyThread2 t1 = new MyThread2(0, 4, 3);
		MyThread2 t2 = new MyThread2(1, 2, 2);

		t1.start();
		t2.start();

		System.out.println("Exited");

	}

}
