package pers.yanxuanshaozhu.datastructure.pharsingarithmeticexpression;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class StackChar2 {
	private int maxSize;
	private int[] stackArray;
	private int top;

	public StackChar2(int size) {
		maxSize = size;
		stackArray = new int[maxSize];
		top = -1;
	}

	public void push(int value) {
		stackArray[++top] = value;
	}

	public int pop() {
		return stackArray[top--];
	}

	public int peek() {
		return stackArray[top];
	}

	public boolean isEmpty() {
		return top == -1;
	}

	public int peekCharN(int n) {
		return stackArray[n];
	}

	public int size() {
		return top + 1;
	}

	public void displayStack(String string) {
		System.out.print(string);
		System.out.print("Stack (bottom-->top): ");
		for (int i = 0; i < size(); i++) {
			System.out.print(peekCharN(i));
			System.out.print(" ");
		}
		System.out.println();
	}
}

class ParsePost {
	private StackChar2 theStackChar;
	private String input;

	public ParsePost(String string) {
		input = string;
	}

	public int doParse() {
		theStackChar = new StackChar2(20);
		char character;
		int i;
		int num1, num2, interAns;
		for (i = 0; i < input.length(); i++) {
			character = input.charAt(i);
			theStackChar.displayStack("" + character + " ");
			if (character >= '0' && character <= '9') {
				theStackChar.push((int) (character - '0'));
			} else {
				num1 = theStackChar.pop();
				num2 = theStackChar.pop();
				switch (character) {
				case '+':
					interAns = num1 + num2;
					break;
				case '-':
					interAns = num1 - num2;
					break;
				case '*':
					interAns = num1 * num2;
					break;
				case '/':
					interAns = num1 / num2;
					break;
				default:
					interAns = 0;
				}
				theStackChar.push(interAns);
			}
		}
		interAns = theStackChar.pop();
		return interAns;
	}
}

public class CalculatePostfix {
	public static void main(String[] args) throws IOException {
		String input;
		int output;

		while (true) {
			System.out.print("Enter postfis:");
			System.out.flush();
			input = getString();
			if (input.equals("")) {
				break;
			}
			ParsePost aParsePost = new ParsePost(input);
			output = aParsePost.doParse();
			System.out.println("Evaluates to " + output);
		}
	}

	public static String getString() throws IOException {
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		String string = br.readLine();
		return string;
	}
}
