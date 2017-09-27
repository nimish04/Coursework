import java.util.Scanner;
import java.lang.System.*;
import java.lang.Math.*;

public class Library
{
	static Scanner sc = new Scanner(System.in);
	static int n1,n2;

	static {
		System.out.println("Welcome to Library Management System");
		System.out.println("1. Genre");
		System.out.println("2. Number of books available");
		System.out.print("Enter choice: ");
		n2 = sc.nextInt();
	}
	static void genres() {
		System.out.println("1. Fiction");
		System.out.println("2. Horror");
		System.out.println("3. Science ");
		System.out.print("Enter choice: ");
		n1 = sc.nextInt();
	}
	static void number() {
		System.out.println("Goosebumps - 55");
		System.out.println("House of the Dead - 996");
		System.out.println("Stargaze - 36");
		System.out.println("Game of Thrones - 42");
		System.out.println("Ghosts - 52");
		System.out.println("Diary of a Wimpy Kid - 18");
		System.out.println("Silent Spring - 154");
		System.out.println("Cosmos - 344");
	}
	void books() {
		switch(n1) {
			case 1:
				System.out.println("1. Goosebumps");
				System.out.println("2. House of the Dead");
				System.out.println("3. Stargaze");
				break;
			case 2:
				System.out.println("1. Game of Thrones");
				System.out.println("2. Ghosts");
				break;
			case 3:
				System.out.println("1. Diary of a Wimpy Kid");
				System.out.println("2. Silent Spring");
				System.out.println("3. Cosmos");
				break;
			default:
			{
				System.out.println("Not available.");
			}
		}
	}
	public static void main(String[] s){
		switch(n2)
		{
			case 1:
				genres();
				Library b = new Library();
				b.books();
				break;
			case 2:
				number();
				break;
			default:
				System.out.println("Not available.");
		}
	}
}