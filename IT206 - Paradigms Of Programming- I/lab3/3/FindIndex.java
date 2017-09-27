import java.util.Scanner;
import java.lang.System.*;

public class FindIndex {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter size of the array: ");
		Integer n = input.nextInt();
		Integer array[] = new Integer[n];
		for (Integer i = 0; i < n; i++) {
			System.out.print("Enter element " + i.toString() + ": ");
			array[i] = input.nextInt();
		}
		System.out.print("Enter the element whose index is to be found: ");
		Integer num = input.nextInt();
		Integer indices[] = new Integer[n];
		Boolean exists = false;
		Integer track = 0;
		for (Integer j = 0; j < n; j++) {
			if (array[j] == num) {
				exists = true;
				indices[track] = j;
				track++;
			}
		}
		if (exists) {
			for (Integer k = 0; k < track; k++) {
				System.out.print(indices[k].toString() + " ");
			}
			System.out.println();
		}
		else {
			System.out.println("Not found!");
		}
	}
}