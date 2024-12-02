import java.io.*;
import java.util.Scanner;

public class PartI {
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
		}
		System.out.println("Final floor: " + floor);
	}
}

// Final floor: 74
