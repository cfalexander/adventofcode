import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;
import java.util.stream.*;

public class PartII {
	public static void main(String[] args) throws Exception {
		BufferedReader reader;
		int total = 0;
		reader = new BufferedReader(new FileReader("input.txt"));
		String line = reader.readLine();
		while (line != null) {
			List<Integer> dimStr = Arrays.asList(line.split("x")).stream().map(Integer::valueOf).collect(Collectors.toList());
			int volume = dimStr.get(0)*dimStr.get(1)*dimStr.get(2);
			dimStr.remove(Collections.max(dimStr));
			total += 2*dimStr.get(0) + 2*dimStr.get(1) + volume;
			line = reader.readLine();
		}
		System.out.println("Total feet of ribbon: " + total);
	}
}
// Total feet of ribbon: 3812909
