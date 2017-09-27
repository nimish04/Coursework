import java.util.Scanner;
import java.lang.System.*;

public class TenSum {
	public static void main(String[] args) {
		System.out.print("Enter size of the array: ");
		Scanner input = new Scanner(System.in);
		Integer n = input.nextInt();
		Integer array[] = new Integer[n];
		for (Integer i = 0; i < n; i++) {
			System.out.print("Enter element " + i.toString() + ": ");
			array[i] = input.nextInt();
		}
		Boolean check = checkFor10s(array);
		System.out.println(check);
	}
	public static Boolean checkFor10s(Integer ar[]) {
		Integer trackSum = 0;
		for (Integer x: ar) {
			if (x == 10) {
				trackSum += 10;
			}
		}
		return (trackSum == 30);
	}
}