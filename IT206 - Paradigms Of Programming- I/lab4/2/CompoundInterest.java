import java.util.*;
import java.lang.System.*;
import java.lang.Math.*;

public class CompoundInterest {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the principle amount: ");
		Float p = input.nextFloat();
		System.out.print("Enter the rate of interest: ");
		Float r = input.nextFloat();
		System.out.print("Enter the number of years: ");
		Integer t = input.nextInt();
		for (Integer i = 1; i <= t; i++) {
			calculate(p, r, i);
		}
	}
	public static void calculate(Float pr, Float ra, Integer ti) {
		Double result = (Double) 1.0 + (ra / 1200.0);
		result = Math.pow(result, 12 * ti);
		result *= pr;
		System.out.println("Year " + ti.toString() + " value: " + result.toString());
	}
}