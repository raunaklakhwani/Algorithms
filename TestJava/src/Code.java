import java.util.Random;

class TrieNode {
	TrieNode1 zeroChild;
	TrieNode1 oneChild;
}

class Trie {
	TrieNode1 root = new TrieNode1();

	void add(int n) {
		TrieNode1 p = root;
		for (int i = 30; i >= 0; i--) {
			if (((n >> i) & 1) == 1) {
				if (p.oneChild == null) {
					p.oneChild = new TrieNode1();
				}
				p = p.oneChild;
			} else {
				if (p.zeroChild == null) {
					p.zeroChild = new TrieNode1();
				}
				p = p.zeroChild;
			}
		}
	}
}

public class Code {
	public static int findMaxBruteForce(int[] array) {
		int max = 0;
		for (int i = 0; i < array.length; i++) {
			int m = 0;
			for (int j = i; j < array.length; j++) {
				m ^= array[j];
				max = Math.max(max, m);
			}
		}
		return max;
	}

	public static int findMaxTrie(int[] array) {
		Trie1 trie = new Trie1();
		trie.add(0);
		int max = 0;
		int cur = 0;
		for (int i = 0; i < array.length; i++) {
			cur ^= array[i];
			TrieNode1 p = trie.root;
			int x = 0;
			for (int j = 30; j >= 0; j--) {
				if (((cur >> j) & 1) == 1) {
					if (p.zeroChild != null) {
						p = p.zeroChild;
					} else {
						x |= (1 << j);
						p = p.oneChild;
					}
				} else {
					if (p.oneChild != null) {
						x |= (1 << j);
						p = p.oneChild;
					} else {
						p = p.zeroChild;
					}
				}
			}
			max = Math.max(max, x ^ cur);
			trie.add(cur);
		}
		return max;
	}

	public static void main(String[] args) {
		int n = 50;
		System.out.println("Ronak");
		int[] array = { 1, 2, 3, 7, 5 };
		/*
		 * Random rand = new Random(); for (int i = 0; i < n; i++) { array[i] =
		 * rand.nextInt(100000) + 1; }
		 */

		int a = findMaxBruteForce(array);
		int b = findMaxTrie(array);

		if (a == b) {
			System.out.println("Algorithm success!");
			System.out.println(String.format("----> %d == %d", a, b));
		} else {
			System.out.println("Algorithm failed!");
			System.out.println(String.format("----> %d != %d", a, b));
		}
	}
}