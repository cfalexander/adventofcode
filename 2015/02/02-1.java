import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Collections;
import java.util.ArrayList;
import java.util.Arrays;

public class PartI {
	public static void main(String[] args) throws Exception {
		BufferedReader reader;
		int total = 0;
		reader = new BufferedReader(new FileReader("input.txt"));
		String line = reader.readLine();
		while (line != null) {
			String[] dimStr = line.split("x");
			int[] dims = new int[3];
			for(int i = 0; i < dims.length; i++) {
				dims[i] = Integer.parseInt(dimStr[i]);
			}
			ArrayList<Integer> comps = new ArrayList<>(Arrays.asList(dims[0]*dims[1], dims[1]*dims[2], dims[0]*dims[2]));
			int slack = Collections.min(comps);
			for (int j = 0; j < comps.size(); j++) {
				total += 2*comps.get(j);
			}
			total += slack;
			line = reader.readLine();
		}
		System.out.println("Total square feet of wrapping paper: " + total);
	}
}
// Total square feet of wrapping paper: 1598415
