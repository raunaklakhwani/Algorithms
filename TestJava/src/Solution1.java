import java.util.Scanner;
import java.util.TreeSet;

public class Solution1 {
	public static Scanner scan = new Scanner(System.in);

	public static void main(String[] args) {
		int t = Integer.parseInt(scan.nextLine().split(" ")[0]);
		

		for (int i = 0; i < t; i++) {
			int curr = 0;
			scan.nextLine();
			String nums = scan.nextLine();
			String[] num = nums.split(" ");
			//System.out.println(num.length);
			TreeSet<Integer> tree = new TreeSet<Integer>();

			for (int j = 0; j < num.length; j++) {
				tree.add(Integer.parseInt(num[j]));
			}
			
			int c = 0;
			while (tree.size() >= 0 && tree.ceiling(curr)!= null){
				int x = tree.ceiling(curr);
				tree.remove(x);
				curr += x;
				c += 1;
			}
			
			System.out.println(c);

		}

	}

}
