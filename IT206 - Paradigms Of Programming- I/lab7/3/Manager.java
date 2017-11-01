package record;

import java.util.Scanner;
import java.lang.System.*;
import java.lang.Math.*;

public class Manager implements ManagerInterface {

	Integer days, holidays;

	public static void main(String[] args) {
		Manager manager = new Manager();
		manager.setup();
		manager.register();
	}

	public void setup() {
		this.days = TOTALDAYS;
		this.holidays = 135;
		System.out.println(this.days);
		System.out.println(this.holidays);
	}

	public void register() {
		System.out.println("Register");
	}
}