import java.util.Scanner;
import java.lang.System.*;

public class Weekdays {
	public static void main(String[] args) {
		System.out.print("Enter an integer between 1 and 7: ");
		Scanner input = new Scanner(System.in);
		Integer n = input.nextInt();
		if ((n > 7) || (n < 1)) {
			System.out.println("Wrong input!");
			return;
		}
		String days[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
		System.out.println(days[n]);
	}
}