import java.util.*;
import java.lang.System.*;
import java.lang.Math.*;

public class Products {
	String barcode;
	String name;
	Float cost;
	static Products prods[];
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Scanner string = new Scanner(System.in);
		System.out.print("Enter the number of products: ");
		Integer n = input.nextInt();
		prods = new Products[n];
		Map<Products, Integer> map = new HashMap<Products, Integer>();
		for (Integer i = 1; i <= n; i++) {
			prods[i - 1] = new Products();
			System.out.print("Enter name for Product " + i.toString() + " : ");
			prods[i - 1].name = input.nextLine();
			prods[i - 1].name = input.nextLine();
			System.out.print("Enter barcode for Product " + i.toString() + " : ");
			prods[i - 1].barcode = input.nextLine();
			System.out.print("Enter price for Product " + i.toString() + " : ");
			prods[i - 1].cost = input.nextFloat();
			map.put(prods[i - 1], 0);
		}
		System.out.println("Choose products you want to buy:");
		while (true) {
			System.out.print("Enter 1 to buy, 2 to display all products or any other number to exit: ");
			Integer choice = input.nextInt();
			if (choice == 1) {
				System.out.print("Enter the product barcode: ");
				String bcd = string.nextLine().replace("\n","");
				for (Map.Entry<Products, Integer> entry : map.entrySet()) {
					if (entry.getKey().barcode.equals(bcd))	 {
						map.put(entry.getKey(), entry.getValue() + 1);
						break;
					}
				}
			}
			else if (choice == 2) {
				for (Integer i = 0; i < n; i++) {
					System.out.println(prods[i].name);
					System.out.println(prods[i].barcode);
					System.out.println(prods[i].cost);
					System.out.println();
				}
			}
			else {
				break;
			}
		}
		Float price = 0.0f;
		for (Map.Entry<Products, Integer> entry : map.entrySet()) {
			System.out.println(entry.getKey().name);
			System.out.println(entry.getKey().barcode);
			System.out.println(entry.getKey().cost);
			System.out.print("Quantity: ");
			System.out.println(entry.getValue());
			System.out.println();
			price += entry.getKey().cost * entry.getValue();
		}
		System.out.println("Total price: " + price.toString());
	}
}