package lakhwani.Exam1;

import java.util.Scanner;

public class Main {

	public static Scanner input = new Scanner(System.in);

	public static int[][] neighbours = { { 1, 0 }, { -1, 0 }, { 0, 1 } };

	public static int maxResult = 0;

	public static void main(String[] args) {
		/**
		 * Input from command line
		 */
		String[] s = input.nextLine().split(" ");
		int rows = Integer.parseInt(s[0]);
		int columns = Integer.parseInt(s[1]);
		
		/**
		 * Grid of dimensions R X C input from command line
		 */
		int[][] grid = new int[rows][columns];
		for (int i = 0; i < rows; i++) {
			String[] row = input.nextLine().split(" ");
			for (int j = 0; j < columns; j++) {
				grid[i][j] = Integer.parseInt(row[j]);
			}
		}

		/**
		 * Visited array of dimensions R X C input from command line to show whether the cell is visited or not.
		 */
		boolean[][] visited = new boolean[rows][columns];


		/**
		 * Call dfs for each cell of the first column.
		 */
		for (int i = 0; i < grid.length; i++) {
			if (grid[i][0] != -1) {
				visited[i][0] = true;
				dfs(grid, i, 0, grid[i][0], visited);
				visited[i][0] = false;
			}
		}

		System.out.println(maxResult);
		input.close();

	}

	
	/**
	 * The idea is to find the maxsum from the current cell(R,C) using the current status of visited array. So using every neighbor of the 
	 * current cell and backtracking after processing is done. Backtracking is done using the visited array which is set to true and after the
	 * cell is processed, it is again reverted to False. Whenever current column C goes outside the grid from the right side, we check the 
	 * currSum and see if it is greater than maxResult. If it is greater than we update the maxResult
	 * @param grid : Grid of dimensions R X C
	 * @param row : Current row
	 * @param column : Current Column
	 * @param currSum : Sum up to the current cell (R,C)
	 * @param visited : Visited array of dimensions R X C to show the current status of visited cells
	 */
	public static void dfs(int[][] grid, int row, int column, int currSum, boolean[][] visited) {
		for (int i = 0; i < neighbours.length; i++) {
			int x = row + neighbours[i][0];
			int y = column + neighbours[i][1];
			if (y == grid[0].length) {
				maxResult = Math.max(maxResult, currSum);
			} else if (x < 0) {
				x = grid.length - 1;
				if (grid[x][y] != -1 && !visited[x][y]) {
					visited[x][y] = true;
					dfs(grid, x, y, grid[x][y], visited);
					visited[x][y] = false;
				}
			} else if (x == grid.length) {
				x = 0;
				if (grid[x][y] != -1 && !visited[x][y]) {
					visited[x][y] = true;
					dfs(grid, x, y, grid[x][y], visited);
					visited[x][y] = false;
				}
			} else if (x >= 0 && x < grid.length) {
				if (grid[x][y] != -1 && !visited[x][y]) {
					visited[x][y] = true;
					dfs(grid, x, y, currSum + grid[x][y], visited);
					visited[x][y] = false;
				}
			}

		}

	}

}
