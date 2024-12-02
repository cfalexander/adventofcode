import java.io.*;
import java.util.Scanner;

public class PartI {
	public static void main(String[] args) throws Exception {
		int total = 0;
		Scanner reader = new Scanner(new File("input.txt"));
		while (reader.hasNext()) {
			String line = reader.next();
			String[] dimStr = line.split("x");
			int[] dims = new int[3];
			for(int i = 0; i < dims.length; i++) {
				dims[i] = Integer.parseInt(dimStr[i]);
			}
			total += 2*dims[0]*dims[1] + 2*dims[1]*dims[2] + 2*dims[0]*dims[2];
		}
		System.out.println("Total square feet of wrapping paper: " + total);
	}
}
