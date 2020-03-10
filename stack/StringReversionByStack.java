package pers.yanxuanshaozhu.datastructure.stack;

import java.util.Scanner;

class CharStack {
	private int maxSize;
	private char[] stackArray;
	private int top;

	public CharStack(int size) {
		maxSize = size;
		stackArray = new char[maxSize];
		top = -1;
	}

	public void push(char i) {
		stackArray[++top] = i;
	}

	public char pop() {
		return stackArray[top--];
	}

	public char peek() {
		return stackArray[top];
	}

	public boolean isEmpty() {
		return (top == -1);
	}

	public boolean isFull() {
		return (top == maxSize - 1);
	}
}

class Reverser {
	private String input;

	Reverser(String input) {
		this.input = input;
	}

	public String reverse() {
		CharStack theStack = new CharStack(input.length());
		for (int i = 0; i < input.length(); i++) {
			char value = input.charAt(i);
			theStack.push(value);
		}

		StringBuffer buffer = new StringBuffer();

		while (!theStack.isEmpty()) {
			buffer.append(theStack.pop());
		}

		return buffer.toString();

	}

}

public class StringReversionByStack {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String string = scanner.next();
		scanner.close();
		System.out.println("The original input:");
		System.out.println(string);
		System.out.println("Inverse of the input:");
		System.out.println(new Reverser(string).reverse());
	}
}
