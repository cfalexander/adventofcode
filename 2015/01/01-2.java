import java.io.*;
import java.util.Scanner;

public class PartII {
	public static void main(String[] args) throws Exception {
		Scanner reader = new Scanner(new File("input.txt"));
		int floor = 0;
		String input = reader.next();
		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) == '(') {
				floor++;
			}
			else if (input.charAt(i) == ')') {
				floor--;
			}
			if (floor == -1) {
				int pos = i + 1;
				System.out.println("First entered basement at position: " + pos + ".");
				break;
			}
		}
	}
}

// First entered basement at position: 1795.
