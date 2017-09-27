import java.util.*;
import java.lang.System.*;
import java.lang.Math.*;

public class VolumeOfShapes {
	public static void main(String[] args) {
		System.out.println("Program to find volume of various shapes.");
		System.out.println("Enter 1 to find volume of a cube");
		System.out.println("Enter 2 to find volume of a cuboid");
		System.out.println("Enter 3 to find volume of a cylinder");
		System.out.println("Enter 4 to find volume of a cone");
		System.out.print("Enter your option: ");
		Scanner input = new Scanner(System.in);
		Integer n = input.nextInt();
		switch (n) {
			case 1:
				System.out.print("Enter the side: ");
				float s = input.nextFloat();
				volume(s);
				break;
			case 2:
				System.out.print("Enter the length: ");
				double ll = input.nextDouble();
				System.out.print("Enter the breadth: ");
				double bb = input.nextDouble();
				System.out.print("Enter the breadth: ");
				double hh = input.nextDouble();
				volume(ll, bb, hh);
				break;
			case 3:
				System.out.print("Enter the radius: ");
				float r = input.nextFloat();
				System.out.print("Enter the height: ");
				float h = input.nextFloat();
				volume(r, h);
				break;
			case 4:
				System.out.print("Enter the radius: ");
				Float rrr = input.nextFloat();
				System.out.print("Enter the height: ");
				Float hhhh = input.nextFloat();
				volume(rrr, hhhh);
				break;
			default:
				break;
		}
	}
	public static void volume(float s) {
		float volume = (float) s * s * s;
		System.out.print("Volume of cube: ");
		System.out.println(volume);
	}
	public static void volume(double l, double b, double h) {
		double volume = (double) l * b * h;
		System.out.print("Volume of cuboid: ");
		System.out.println(volume);
	}
	public static void volume(float r, float h) {
		float volume = (float) 3.14f * r * r * h;
		System.out.print("Volume of a cylinder: ");
		System.out.println(volume);
	}
	public static void volume(Float r, Float h) {
		Float constant = 3.14f / 3.0f;
		Float volume = (Float) constant * r * r * h;
		System.out.print("Volume of cone: ");
		System.out.println(volume);
	}
}