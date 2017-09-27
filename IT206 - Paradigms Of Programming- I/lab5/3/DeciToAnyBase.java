import java.util.Scanner;
import java.lang.System.*;

public class DeciToAnyBase {
	public static void main(String[] args) {
		System.out.println("Decimal to any Base Conversion");
		System.out.print("Enter the Decimal number: ");
		Scanner input = new Scanner(System.in);
		Integer number = input.nextInt();
		System.out.print("Enter the base you want to convert it to: ");
		Integer base = input.nextInt();
		Integer rem;
		String bin = "";
		while (number != 0) {
			rem = number % base;
			if (rem < 10) {
				bin = Integer.toString(rem) + bin;
			}
			else {
				int temp = rem + 55;
				bin = Character.toString((char) temp) + bin;
			}
			number /= base;
		}
		System.out.println(bin);
	}
}