import java.util.Scanner;

class CG {

	int num;

	int numClues;

	CG(int num, int numClues) {

		this.num = num;

		this.numClues = numClues;

	}

}

public class Main {

	public static void main(String[] args) {

		// TODO Auto-generated method stub

		Scanner inp = new Scanner(System.in);

		int numCase = inp.nextInt();

		CG[] arr = new CG[numCase];

		for (int i = 0; i < numCase; i++) {

			int num = inp.nextInt();

			int numClues = inp.nextInt();

			arr[i] = new CG(num, numClues);

		}

		compute(arr, numCase);
		//System.out.println("Ronak");
		inp.close();

	}

	static void compute(CG[] arr, int N) {

		for (int i = 1000; i <= 9999; i++) {

			if (match(i, arr)) {

				System.out.println(i);

				break;

			}

		}

	}

	static boolean match(int i, CG[] arr) {

		String s = "" + i;
		for (int i1 = 0; i1 < arr.length; i1++) {
			CG cg = arr[i1];
			String num = "" + cg.num;

			int count = 0;

			for (int i2 = 0; i2 < num.length(); i2++) {

				if (s.charAt(i2) == num.charAt(i2)) {

					count++;

				}

			}

			if (count != cg.numClues) {

				return false;

			}

		}

		return true;

	}

}
