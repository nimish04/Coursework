interface ActualInterface {
	void display1();
	void display2();
}

abstract class AbstractImplement implements ActualInterface {
	public void display1() {
		System.out.println("AbstractImplement.");
	}

	abstract void whoAmI();
}

public class PartialInterface extends AbstractImplement {

	public void whoAmI() {
		System.out.println("PartialInterface.");
	}

	public void display2() {
		System.out.println("ActualInterface in PartialInterface.");
	}

	public static void main(String[] args) {
		PartialInterface obj = new PartialInterface();
		obj.display1();
		obj.display2();
		obj.whoAmI();
	}
}