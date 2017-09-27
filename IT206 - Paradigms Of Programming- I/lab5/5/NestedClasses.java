import java.util.*;
import java.lang.System.*;
import java.lang.Math.*;

public class NestedClasses {
	public static void main(String[] args) {
		OuterClass.InnerStatic staticobj = new OuterClass.InnerStatic();
		staticobj.display();
		OuterClass.InnerMethod instobj = new OuterClass().new InnerMethod();
		instobj.display();
	}
}

class OuterClass {
	static String st = "staticvar";
	String ins = "instancevar";
	static class InnerStatic {
		void display() {
			System.out.println(st);
		}
	}
	class InnerMethod {
		void display() {
			System.out.println(ins);
		}
	}
}