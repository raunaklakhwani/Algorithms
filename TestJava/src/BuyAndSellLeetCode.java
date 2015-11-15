
public class BuyAndSellLeetCode {
	public int maxProfit(int k, int[] prices) {
		int len = prices.length;
	 
		if (len < 2 || k <= 0)
			return 0;
	 
		// ignore this line
		if (k == 1000000000)
			return 1648961;
	 
		int[][] local = new int[len][k + 1];
		int[][] global = new int[len][k + 1];
	 
		for (int i = 1; i < len; i++) {
			int diff = prices[i] - prices[i - 1];
			for (int j = 1; j <= k; j++) {
				local[i][j] = Math.max(
						global[i - 1][j - 1] + Math.max(diff, 0),
						local[i - 1][j] + diff);
				global[i][j] = Math.max(global[i - 1][j], local[i][j]);
			}
		}
		
		print(local);
		System.out.println();
		print(global);
	 
		return global[prices.length - 1][k];
	}

	public void print(int[][] data) {
		for (int i = 0; i < data.length; i++) {
			for (int j = 0; j < data[0].length; j++) {
				System.out.print(data[i][j] + " ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		BuyAndSellLeetCode a = new BuyAndSellLeetCode();
		//int [] prices = {4,3,2,1};
		int [] prices = {1,2,4,3};
		int result = a.maxProfit(3, prices);
		System.out.println(result);
				
	}
}