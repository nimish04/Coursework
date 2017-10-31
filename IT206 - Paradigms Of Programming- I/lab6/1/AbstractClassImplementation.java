import java.util.Scanner;
import java.lang.System.*;
import java.lang.Math.*;

public class AbstractClassImplementation {
	public static void main(String[] args) {
		Dog dogSound = new Dog();
		Cat catSound = new Cat();
		Elephant elephantSound = new Elephant();
		dogSound.makeSound();
		catSound.makeSound();
		elephantSound.makeSound();
		elephantSound.whatDoIDo();
	}
}

abstract class SoundMaker {
	abstract void makeSound();

	void whatDoIDo() {
		System.out.println("I make sounds.");
	}
}

class Dog extends SoundMaker {
	void makeSound() {
		System.out.println("Dog Sound!");
	}
}

class Cat extends SoundMaker {
	void makeSound() {
		System.out.println("Cat Sound!");
	}
}

class Elephant extends SoundMaker {
	void makeSound() {
		System.out.println("Elephant Sound!");
	}
}