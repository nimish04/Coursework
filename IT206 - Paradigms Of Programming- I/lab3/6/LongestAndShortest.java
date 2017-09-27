import java.util.*;
import java.lang.System.*;

public class LongestAndShortest {
	public static void main(String[] args) {
		System.out.print("Enter length of the array: ");
		Scanner input = new Scanner(System.in);
		Integer n = input.nextInt();
		Float array[] = new Float[n];
		for (Integer i = 0; i < n; i++) {
			System.out.print("Enter element " + i.toString() + ": ");
			array[i] = input.nextFloat();
		}
		Float sorted[] = bubbleSort(array);
		Integer index = 1, counter = 1, greatest = 1, least = n;
		while (index < n) {
			if (sorted[index] == (sorted[index - 1] + 1)) {
				counter++;
			}
			else {
				if (counter > greatest) {
					greatest = counter;
				}
				if (counter < least) {
					least = counter;
				}
				counter = 1;
			}
			index++;
		}
		System.out.println("Sorted: " + Arrays.toString(sorted));
		System.out.println("Greatest: " + Integer.toString(greatest));
		System.out.println("Least: " + Integer.toString(least));
	}
	public static Float[] bubbleSort(Float[] arr) {
		Float ar[] = arr;
		Float temp;
		for (Integer a = 0; a < ar.length - 1; a++) {
			for (Integer b = 0; b < ar.length - a - 1; b++) {
				if (ar[b] > ar[b + 1]) {
					temp = ar[b + 1];
					ar[b + 1] = ar[b];
					ar[b] = temp;
				}
			}
		}
		return ar;
	}
}