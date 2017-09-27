import java.util.Scanner;
import java.lang.System.*;

public class StudentDetails {
	String rollNo;
	String name;
	Float cgpa;
	Integer semester;
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the number of student records you want to input: ");
		Integer n = input.nextInt();
		StudentDetails records[] = new StudentDetails[n];
		for (Integer i = 0; i < n; i++) {
			records[i] = new StudentDetails();
			Integer store = i + 1;
			System.out.println("Details of Student " + store.toString());
			System.out.print("Enter roll number: ");
			records[i].rollNo = input.nextLine();
			records[i].rollNo = input.nextLine();
			System.out.print("Enter name: ");
			records[i].name = input.nextLine();
			System.out.print("Enter CGPA: ");
			records[i].cgpa = input.nextFloat();
			System.out.print("Enter Semester: ");
			records[i].semester = input.nextInt();
		}
		for (Integer k = 0; k < n; k++) {
			Integer store = k + 1;
			System.out.println("Details of Student " + store.toString());
			System.out.println("Semester " + records[k].semester.toString());
			System.out.println("Name " + records[k].name);
			System.out.println("Roll Number " + records[k].rollNo);
			System.out.println("CGPA " + records[k].cgpa.toString());
		}
	}
}