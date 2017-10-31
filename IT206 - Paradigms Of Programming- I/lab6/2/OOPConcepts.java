import java.io.Serializable;
import java.awt.*;  
import java.awt.event.*;  

interface Horror {
	abstract class Scarface {
		abstract void getPart();
		void getName() {
			System.out.println("Scarface");
		}
	}
}

class Movies extends Horror.Scarface {
	public void getPart() {
		System.out.println("All parts hihihahahaha");
	}
}

interface TVChannels {
	void channelPack();
}

interface Cartoon extends TVChannels {
	String category = "Kids";
	void show();
	interface Pogo {
		void rating();
	}
}

class TV implements Cartoon, Cartoon.Pogo {
	public void show() {
		System.out.println("Courage the Cowardly Dog");
	}
	public void channelPack() {
		System.out.println("Children's Pack");
	}
	public void rating() {
		System.out.println("Best rated!");
	}
}

class Animal implements Cloneable {
	String name;
 
	public Animal(String name) {
		this.name = name;
	}

	interface Sound {
		void makeSound();
	}

	@Override
	protected Object clone() throws CloneNotSupportedException {
		return super.clone();
	}
}

class DogBark implements Animal.Sound {
	public void makeSound() {
		System.out.println("Bark!");
	}
}

class AdapterExample {  
	Frame f;
	AdapterExample() {
	    f = new Frame("Window Adapter");
	    f.addWindowListener(new WindowAdapter() {
	        public void windowClosing(WindowEvent e) {  
	            f.dispose();
	        }
	    });
	    f.setSize(400,400);
	    f.setLayout(null);
	    f.setVisible(true);
	}
}
 
public class OOPConcepts {
	public static void main(String[] args) throws CloneNotSupportedException {
		Animal cheetah = new Animal("Cheetah");
		Animal cheetah2 = (Animal) cheetah.clone();
		System.out.println(cheetah.name);
		System.out.println(cheetah2.name);
		DogBark dogBark = new DogBark();
		Animal.Sound bark = dogBark;
		bark.makeSound();
		TV newTV = new TV();
		newTV.channelPack();
		newTV.show();
		System.out.println(newTV.category);
		newTV.rating();
		Movies newMovie = new Movies();
		newMovie.getPart();
		newMovie.getName();
		AdapterExample newFrame = new AdapterExample();
	}
}