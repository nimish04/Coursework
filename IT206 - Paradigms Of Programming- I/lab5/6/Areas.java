import java.util.Scanner;
import java.lang.System.*;
import java.lang.Math.*;

public class Areas {
	float ra;
	double rad;
	float hei;
	double heig;
	float len;
	float brea;
	Float bas;
	Float heigh;
	Areas(float r, float h) {
		this.ra = r;
		this.hei = h;
		area(this.ra, this.hei);
	}
	Areas(double r, double h) {
		this.rad = r;
		this.heig = h;
		area(this.rad, this.heig);
	}
	Areas(float l, float b, float h) {
		this.len = l;
		this.brea = b;
		this.hei = h;
		area(this.len, this.brea, this.hei);
	}
	Areas(Float s, Float h) {
		this.bas = s;
		this.heigh = h;
		area(this.bas, this.heigh);
	}
	Areas(float r) {
		this.ra = r;
		area(this.ra);
	}
	public static void main(String[] args) {
		System.out.println("Program to find area of various shapes.");
		System.out.println("Enter 1 to find area of a cone");
		System.out.println("Enter 2 to find area of a cylinder");
		System.out.println("Enter 3 to find area of a rectangular prism");
		System.out.println("Enter 4 to find area of a pyramid");
		System.out.println("Enter 5 to find area of a hemisphere");
		System.out.print("Enter your option: ");
		Scanner input = new Scanner(System.in);
		Integer n = input.nextInt();
		switch (n) {
			case 1:
				System.out.print("Enter the radius: ");
				float r = input.nextFloat();
				System.out.print("Enter the height: ");
				float h = input.nextFloat();
				Areas coneobj = new Areas(r, h);
				break;
			case 2:
				System.out.print("Enter the radius: ");
				double rr = input.nextDouble();
				System.out.print("Enter the height: ");
				double hh = input.nextDouble();
				Areas cylobj = new Areas(rr, hh);
				break;
			case 3:
				System.out.print("Enter the length: ");
				float l = input.nextFloat();
				System.out.print("Enter the breadth: ");
				float b = input.nextFloat();
				System.out.print("Enter the height: ");
				float hhh = input.nextFloat();
				Areas prismobj = new Areas(l, b, hhh);
				break;
			case 4:
				System.out.print("Enter the base side: ");
				Float rrr = input.nextFloat();
				System.out.print("Enter the height: ");
				Float hhhh = input.nextFloat();
				Areas pyramobj = new Areas(rrr, hhhh);
				break;
			case 5:
				System.out.print("Enter the radius: ");
				float rrrr = input.nextFloat();
				Areas hemiobj = new Areas(rrrr);
				break;
			default:
				break;
		}
	}
	public static void area(float r, float h) {
		float first = (float) 3.14 * r * r;
		float l = (float) Math.sqrt(h * h + r * r);
		float second = (float) 3.14 * r * l;
		float area = (float) first + second;
		System.out.print("Area of cone: ");
		System.out.println(area);
	}
	public static void area(double r, double h) {
		double area = (double) 3.14 * r * r * h;
		System.out.print("Area of cylinder: ");
		System.out.println(area);
	}
	public static void area(float l, float b, float h) {
		float area = (float) 2.0 * (l * b + b * h + l * h);
		System.out.print("Area of rectangular prism: ");
		System.out.println(area);
	}
	public static void area(Float s, Float h) {
		Float area = (Float) (s * s * h);
		area /= (Float) 3.0f	;
		System.out.print("Area of pyramid: ");
		System.out.println(area);
	}
	public static void area(float r) {
		float area = (float) (3.0 * 3.14 * ((float) Math.pow(r, 2)));
		System.out.print("Area of hemisphere: ");
		System.out.println(area);
	}
}