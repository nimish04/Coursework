import java.util.Scanner;
import java.lang.System.*;

public class Calculator {
	public static void main(String[] args) {
		System.out.println("CALCULATOR");
		System.out.print("Enter 1 for addition, 2 for substraction, 3 for multiplication and 4 for division: ");
		Scanner input = new Scanner(System.in);
		Integer option = input.nextInt();
		float a, b;
		switch (option) {
			case 1:
				System.out.print("Enter first number: ");
				a = input.nextFloat();
				System.out.print("Enter second number: ");
				b = input.nextFloat();
				System.out.println(a + b);
				break;
			case 2:
				System.out.print("Enter first number: ");
				a = input.nextFloat();
				System.out.print("Enter second number: ");
				b = input.nextFloat();
				System.out.println(a - b);
				break;
			case 3:
				System.out.print("Enter first number: ");
				a = input.nextFloat();
				System.out.print("Enter second number: ");
				b = input.nextFloat();
				System.out.println(a * b);
				break;
			case 4:
				System.out.print("Enter first number: ");
				a = input.nextFloat();
				System.out.print("Enter second number: ");
				b = input.nextFloat();
				if (b == 0) {
					System.out.println("Division by 0 error!");
					break;
				}
				System.out.println(a / b);
				break;
			default:
				System.out.println("Wrong option!");
				break;
		}
	}
}