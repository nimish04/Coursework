import java.util.*;
import java.lang.System.*;
import java.lang.Math.*;

public class NestedTryCatchStatements {
	public static void main(String[] args) {
		Integer a = 25;
		ArrayList<Integer> numbers = new ArrayList<>();
		numbers.add(0, 0);
		numbers.add(0, 5);
		numbers.add(0, 10);
		Random gen = new Random();
		Integer store;
		Integer chosen = numbers.get(gen.nextInt(numbers.size()));
		try {
			store = a / chosen;
			System.out.println("Success!");
		}
		catch (ArithmeticException e) {
			System.out.println("Oops! Arithmetic Error!");
			chosen = numbers.get(gen.nextInt(numbers.size()));
			try {
				store = a / chosen;
			}
			catch (ArithmeticException f) {
				System.out.println("Caught again in Arithmetic Error!");
			}
		}
		catch (Exception e) {
			System.out.println("Something went wrong!");
		}
	}
}