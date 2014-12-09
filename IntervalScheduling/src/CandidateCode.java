import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Booking implements Comparable<Booking> {
	public String start;
	public String end;
	public int startIndex;
	public int endIndex;
	public String status = "active";

	public Booking(String start, String end, int startIndex, int endIndex) {
		super();
		this.start = start;
		this.end = end;
		this.startIndex = startIndex;
		this.endIndex = endIndex;
	}

	@Override
	public int compareTo(Booking o) {
		if (endIndex > o.endIndex)
			return 1;
		else if (endIndex < o.endIndex)
			return -1;
		else {
			return startIndex < o.startIndex ? 1 : -1;
		}
	}

	@Override
	public String toString() {
		String toString = start + ":" + end;
		return toString;
	}

	public boolean isOverlap(Booking b1) {
		if (b1.startIndex < endIndex && b1.endIndex >= endIndex) {
			return true;
		} else {
			return false;
		}

	}

}

public class CandidateCode {

	static ArrayList<Booking> inputList = new ArrayList<Booking>();
	static int[] timing = new int[24];

	public static void main(String[] args) {
		String[] input = { "6AM#8AM", "11AM#1PM", "7AM#3PM", "7AM#10AM",
				"10AM#12PM", "2PM#4PM", "1PM#4PM", "8AM#9AM" };
		preProcessInput(input);
		Collections.sort(inputList);
		for (Booking b : inputList) {
			System.out.println(b);
		}
		int count = inputList.size();
		for (int index = 0; index < inputList.size(); index++) {
			Booking b = inputList.get(index);
			if (b.status.equalsIgnoreCase("active")) {
				for (int j = index + 1; j < inputList.size(); j++) {
					Booking con = inputList.get(j);
					if (b.isOverlap(con)
							&& con.status.equalsIgnoreCase("active")) {
						con.status = "Deleted";
						count--;
					}
				}
			}
		}

		System.out.println(count);

	}

	public static int getTimeIndex(String time) {
		int timeIndex = 0;
		if (time.indexOf("AM") != -1) {
			timeIndex = Integer.parseInt(time.substring(0, time.indexOf("AM")));
			if (timeIndex == 12) {
				timeIndex = 0;
			}
			return timeIndex;
		} else {
			timeIndex = Integer.parseInt(time.substring(0, time.indexOf("PM")));
			if (timeIndex == 12) {
				timeIndex = 0;
			}
			return timeIndex + 12;
		}
	}

	public static void preProcessInput(String[] input) {

		for (int i = 0; i < input.length; i++) {
			String element = input[i];
			String start = element.substring(0, element.indexOf("#"));
			String end = element.substring(element.indexOf("#") + 1);
			int startTimingIndex = getTimeIndex(start);
			int endTimingIndex = getTimeIndex(end);

			Booking booking = new Booking(start, end, startTimingIndex,
					endTimingIndex);
			inputList.add(booking);
		}
	}

	public static int jobMachine(String[] input1) {
		preProcessInput(input1);
		Collections.sort(inputList);
		for (Booking b : inputList) {
			System.out.println(b);
		}
		int count = inputList.size();
		for (int index = 0; index < inputList.size(); index++) {
			Booking b = inputList.get(index);
			if (b.status.equalsIgnoreCase("active")) {
				for (int j = index + 1; j < inputList.size(); j++) {
					Booking con = inputList.get(j);
					if (b.isOverlap(con)
							&& con.status.equalsIgnoreCase("active")) {
						con.status = "Deleted";
						count--;
					}
				}
			}
		}
		return count * 500;
	}
}
