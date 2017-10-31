import java.util.*;
import java.lang.System.*;
import java.lang.Math.*;

public class ThrowExceptionStatements {
	public static void main(String[] args) {
		Integer a = 25;
		ArrayList<Integer> numbers = new ArrayList<>();
		numbers.add(0, 0);
		numbers.add(0, 5);
		numbers.add(0, 10);
		Random gen = new Random();
		Integer chosen = numbers.get(gen.nextInt(numbers.size()));
		if (chosen == 0)
			throw new ArithmeticException("No division by 0!");
		else
			System.out.println(a / chosen);
	}
}