import java.util.Scanner;
import java.lang.System.*;

public class BitWise {
	public static void main(String[] args) {
		System.out.println("Implementing left shift, right shift and right shift unsigned");
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the number: ");
		Integer a = input.nextInt();
		System.out.print("Enter the shift: ");
		Integer shift = input.nextInt();
		System.out.print("Left shift: ");
		System.out.println(a << shift);
		System.out.print("Right shift: ");
		System.out.println(a >> shift);
		System.out.print("Right unsigned shift: ");
		System.out.println(a >>> shift);
	}
}