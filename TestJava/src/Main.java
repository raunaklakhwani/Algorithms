import java.util.Arrays;

public class Main{
	public static void main(String[] args) {
		char[] ch = new char[Integer.MAX_VALUE - 1];
		Arrays.fill(ch, 'a');
		String s = new String(ch);
		System.out.println(s);
				
	}
}