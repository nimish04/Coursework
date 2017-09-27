import java.util.Scanner;
import java.lang.System.*;
import java.util.*;

public class CheckOrder {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Integer[] numbers = new Integer[3];
		System.out.print("Enter first number: ");
		numbers[0] = input.nextInt();
		System.out.print("Enter second number: ");
		numbers[1] = input.nextInt();
		System.out.print("Enter third number: ");
		numbers[2] = input.nextInt();
		Integer[] originalNumbers = {numbers[0], numbers[1], numbers[2]};
		Integer[] reverseNumbers = {numbers[0], numbers[1], numbers[2]};
		Arrays.sort(numbers);
		Arrays.sort(reverseNumbers, Collections.reverseOrder());
		System.out.println(Arrays.toString(numbers));
		if (Arrays.equals(originalNumbers, numbers)) {
			System.out.println("Increasing order.");
		}
		else if (Arrays.equals(originalNumbers, reverseNumbers)) {
			System.out.println("Decreasing order.");
		}
		else {
			System.out.println("Neither increasing nor decreasing order.");
		}
	}
}