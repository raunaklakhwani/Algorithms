import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

class Node implements Comparable<Node> {
	int element;
	int index;
	int currIndex;

	Node(int element, int index, int currIndex) {
		this.element = element;
		this.index = index;
		this.currIndex = currIndex;
	}

	@Override
	public int compareTo(Node o) {
		if (element > o.element) {
			return 1;
		}
		return -1;
	}

}

class Heap {

	public void buildHeap(Node[] nodes) {

		for (int i = nodes.length / 2 + 1; i >= 0; i--) {
			percolateDown(nodes, i);
		}

	}

	public void percolateDown(Node[] nodes, int index) {
		while (index < nodes.length) {
			if ((2 * index + 1) < nodes.length) {
				int max = nodes[2 * index + 1].element;
				int maxi = 2 * index + 1;
				if ((2 * index + 2) < nodes.length) {
					if (max < nodes[2 * index + 2].element) {
						max = nodes[2 * index + 2].element;
						maxi = 2 * index + 2;
					}
				}

				if (nodes[index].element > max) {
					swapNodes(nodes, index, maxi);
					index = maxi;
				} else {
					break;
				}
			} else {
				break;
			}

		}

	}

	public void swapNodes(Node[] nodes, int a, int b) {
		Node temp = nodes[a];
		nodes[a] = nodes[b];
		nodes[b] = temp;
	}

}

public class Main2 {
	public static void main(String[] args) {
		int[][] m = { { 10, 20, 30, 40 }, { 15, 25, 35, 45 }, { 25, 29, 37, 48 }, { 32, 33, 39, 50 } };
		int k = 16;
		PriorityQueue<Node> heap = new PriorityQueue<Node>();
		for (int i = 0; i < m.length; i++) {
			Node node = new Node(m[0][i], i, 0);
			heap.add(node);
		}

		int count = 0;
		while (heap.size() != 0) {
			Node node = heap.poll();
			count++;
			if (count == k) {
				System.out.println(node.element + " " + node.index);
				break;
			}
			if (node.currIndex + 1 < m.length) {
				Node newNode = new Node(m[node.currIndex + 1][node.index], node.index, node.currIndex + 1);
				heap.add(newNode);
			}
		}

	}
}
