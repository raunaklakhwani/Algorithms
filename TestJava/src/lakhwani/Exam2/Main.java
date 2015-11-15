package lakhwani.Exam2;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.Queue;

public class Main {

	public static Scanner input = new Scanner(System.in);

	public static void main(String[] args) {
		String[] s = input.nextLine().split(" ");
		int numCities = Integer.parseInt(s[0]);
		int numQueries = Integer.parseInt(s[1]);

		List<List<Integer>> adjacencyList = new ArrayList<List<Integer>>(numCities);//adj list to represent the graph
		
		boolean[] isFestiveCity = new boolean[numCities]; //Boolean to indicate whether city is festive or not
		isFestiveCity[0] = true;
		
		/*
		 * Initialization of adjacency list
		 */
		for (int i = 0; i < numCities; i++) {
			List<Integer> x = new ArrayList<Integer>();
			adjacencyList.add(x);
		}

		/**
		 * Creation of adjacency list
		 */
		for (int i = 0; i < numCities - 1; i++) {
			String[] s1 = input.nextLine().split(" ");
			int a = Integer.parseInt(s1[0]);
			int b = Integer.parseInt(s1[1]);
			adjacencyList.get(a - 1).add(b - 1);
			adjacencyList.get(b - 1).add(a - 1);
		}

		
		/**
		 * Loop to answer the Queries
		 */
		for (int i = 0; i < numQueries; i++) {
			String[] s1 = input.nextLine().split(" ");
			int queryType = Integer.parseInt(s1[0]);
			int currCity = Integer.parseInt(s1[1]);

			if (queryType == 1) {
				// Make the city as festival city
				isFestiveCity[currCity - 1] = true;
			} else {
				getClosestCity(adjacencyList, isFestiveCity, currCity);
			}

		}
		
		input.close();

	}

	/**
	 * Method to do the BFS search for finding the nearest festival city
	 * @param adjacencyList : Represents the adjacency list of the island
	 * @param isFestiveCity : Array showing whether the city is a festiveCity or not
	 * @param currCity : City where you are currently
	 */
	public static void getClosestCity(List<List<Integer>> adjacencyList, boolean[] isFestiveCity, int currCity) {
		Queue<List<Integer>> queue = new LinkedList<List<Integer>>();
		List<Integer> l = new ArrayList<Integer>();
		l.add(currCity-1);
		l.add(0);
		queue.add(l);

		while (!queue.isEmpty()) {
			List<Integer> l1 = queue.poll();
			int item = l1.get(0);
			int count = l1.get(1);
			// If festival city found then print the count
			if (isFestiveCity[item]) {
				System.out.println(count);
				break;
			} else {
				// Put the adjacent cities in the queue and keep an eye that same vertex is not put into the queue
				for (int k = 0; k < adjacencyList.get(item - 1).size(); k++) {
					int next = adjacencyList.get(item - 1).get(k);
					if (next != item) {
						List<Integer> l2 = new ArrayList<Integer>();
						l2.add(next);
						l2.add(count + 1);
						queue.add(l2);
					}
				}
			}

		}
	}

}
