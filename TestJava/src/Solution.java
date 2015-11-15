import java.util.Arrays;
import java.util.Scanner;

class IntervalsPicker {
	private class Interval implements Comparable<Interval> {
		int start, end;

		public Interval(int start, int end) {
			this.start = start;
			this.end = end;
		}

		@Override
		public int compareTo(Interval that) {
			if (this.end != that.end)
				return this.end - that.end;
			else
				return this.start - that.start;
			
			
		}

		public String toString() {
			return "[" + start + " " + end + "]";
		}
	}

	private final Interval[] intervals;

	public IntervalsPicker(int[] starts, int[] ends) {
		assert starts.length == ends.length;
		this.intervals = new Interval[starts.length];

		for (int i = 0; i < starts.length; i++) {
			this.intervals[i] = new Interval(starts[i], ends[i]);
		}

		Arrays.sort(this.intervals);
	}

	public int getLargestNonoverlappingSubsetSize() {
		if (intervals.length < 3)
			return intervals.length;

		Interval prelastAcceptedInterval = intervals[0];
		Interval lastAcceptedInterval = intervals[1];
		int lastDouble = -1;
		if (prelastAcceptedInterval.end >= lastAcceptedInterval.start)
			lastDouble = prelastAcceptedInterval.end;

		int intervalsCounter = 2;

		for (int i = 2; i < intervals.length; i++) {
			Interval newInterval = intervals[i];

			if (newInterval.start > lastDouble) {
				intervalsCounter++;
				prelastAcceptedInterval = lastAcceptedInterval;
				lastAcceptedInterval = newInterval;

				if (prelastAcceptedInterval.end >= lastAcceptedInterval.start)
					lastDouble = prelastAcceptedInterval.end;
			}
		}

		return intervalsCounter;
	}
}

public class Solution {

	public static void main(String[] args) {
		final Scanner scanner = new Scanner(System.in);

		int numberOfTestCases = scanner.nextInt();

		for (int testCaseNumber = 0; testCaseNumber < numberOfTestCases; testCaseNumber++) {
			int numberOfIntervals = scanner.nextInt();
			int[] starts = new int[numberOfIntervals];
			int[] ends = new int[numberOfIntervals];

			for (int i = 0; i < numberOfIntervals; i++) {
				starts[i] = scanner.nextInt();
				ends[i] = scanner.nextInt();

			}

			final IntervalsPicker picker = new IntervalsPicker(starts, ends);
			int largestNonoverlappingSubset = picker.getLargestNonoverlappingSubsetSize();
			System.out.println(largestNonoverlappingSubset);
		}
		scanner.close();
	}

}