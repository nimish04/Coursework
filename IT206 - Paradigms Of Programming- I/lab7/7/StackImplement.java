import java.util.*;

interface ADT {
	void push(Integer element);
	Integer pop();
	Integer get(Integer n);
}
class StackImplement implements ADT {

	ArrayList<Integer> list = new ArrayList<>();

	public void push(Integer element) {
		list.add(0, element);
	}

	public Integer pop() {
		Integer toret = list.get(0);
		list.remove(0);
		return toret;
	}

	public Integer get(Integer n) {
		return list.get(n);
	}

	public static void main(String[] args) {
		StackImplement st = new StackImplement();
		st.push(5);
		st.push(10);
		st.push(15);
		System.out.println(st.pop());
		System.out.println(st.get(0));
	}
}