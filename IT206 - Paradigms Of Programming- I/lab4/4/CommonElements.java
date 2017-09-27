import java.lang.System.*;
import java.util.*;

public class CommonElements {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter length for the first array: ");
		Integer length1 = input.nextInt();
		Integer[] first = new Integer[length1];
		for (Integer i = 0; i < length1; i++) {
			System.out.print("Enter element " + Integer.toString(i) + ": ");
			first[i] = input.nextInt();
		}
		System.out.print("Enter length for the second array: ");
		Integer length2 = input.nextInt();
		Integer[] second = new Integer[length2];
		for (Integer i = 0; i < length2; i++) {
			System.out.print("Enter element " + Integer.toString(i) + ": ");
			second[i] = input.nextInt();
		}
		Integer counter = 0;
		if (length2 >= length1) {
			for (Integer j = 0; j < length2; j++) {
				if (Arrays.asList(first).contains(second[j])) {
					counter++;
				}
			}
		}
		else {
			for (Integer j = 0; j < length1; j++) {
				if (Arrays.asList(second).contains(first[j])) {
					counter++;
				}
			}
		}
		System.out.println("Number of common elements: " + counter.toString());
	}
}