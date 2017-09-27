import java.util.*;
import java.lang.System.*;
import java.lang.Math.*;

public class StudentScore {
	Float score[];
	static StudentScore studs[];
	public Float calculate() {
		Float toret = 0.0f;
		for (Integer s = 0; s < 4; s++) {
			toret += this.score[s];
		}
		return toret;
	}
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter number of students: ");
		Integer n = input.nextInt();
		studs = new StudentScore[n];
		for (Integer i = 1; i <= n; i++) {
			studs[i - 1] = new StudentScore();
			studs[i - 1].score = new Float[5];
			for (Integer j = 1; j <= 5; j++) {
				System.out.print("Enter score for student " + i.toString() + " and subject " +j.toString() + ": ");
				studs[i - 1].score[j - 1] = input.nextFloat();
			}
		}
		for (Integer m = 1; m <= n; m++) {
			System.out.print("Total score for student " + m.toString() + ": ");
			System.out.println(studs[m - 1].calculate());
		}
	}
}