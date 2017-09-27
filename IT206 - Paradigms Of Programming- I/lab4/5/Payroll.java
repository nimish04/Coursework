import java.util.*;
import java.lang.System.*;
import java.lang.Math.*;

public class Payroll {
	String employeeNo;
	String name;
	Float salary;
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the number of employee records you want to input: ");
		Integer n = input.nextInt();
		Payroll records[] = new Payroll[n];
		for (Integer i = 0; i < n; i++) {
			records[i] = new Payroll();
			Integer store = i + 1;
			System.out.println("Details of Employee " + store.toString());
			System.out.print("Enter employee number: ");
			records[i].employeeNo = input.nextLine();
			records[i].employeeNo = input.nextLine();
			System.out.print("Enter name: ");
			records[i].name = input.nextLine();
			System.out.print("Enter Salary: ");
			records[i].salary = input.nextFloat();
		}
		for (Integer k = 0; k < n; k++) {
			Integer store = k + 1;
			System.out.println("Details of Employee " + store.toString());
			System.out.println("Employee number " + records[k].employeeNo);
			System.out.println("Name " + records[k].name);
			System.out.println("Salary " + records[k].salary.toString());
			System.out.println("Payroll " + calculate(records[k].salary));
		}
	}

	public static String calculate(Float s) {
		Float dp = 0.5f * s;
		Float da = 0.35f * (dp + s);
		Float hra = 0.08f * (dp + s);
		Float ma = 0.03f * (dp + s);
		Float pf = 0.1f * (dp + s);
		Float result = s + dp + da + hra + ma - pf;
		return result.toString();
	}
}