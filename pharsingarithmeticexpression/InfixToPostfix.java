package pers.yanxuanshaozhu.datastructure.pharsingarithmeticexpression;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class StackChar1 {
	private int maxSize;
	private char[] stackArray;
	private int top;

	public StackChar1(int size) {
		maxSize = size;
		stackArray = new char[maxSize];
		top = -1;
	}

	public void push(char value) {
		stackArray[++top] = value;
	}

	public char pop() {
		return stackArray[top--];
	}
	
	public char peek() {
		return stackArray[top];
	}
	
	public boolean isEmpty() {
		return top == -1;
	}

	public char peekCharN(int n) {
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

class InToPost {
	private StackChar1 theStackChar;
	private String input;
	private String output = "";

	public InToPost(String input) {
		this.input = input;
		int stackSize = input.length();
		theStackChar = new StackChar1(stackSize);
	}

	public String doTrans() {
		for (int i = 0; i < input.length(); i++) {
			char character = input.charAt(i);
			theStackChar.displayStack("For " + character + " ");
			switch (character) {
			case '+':
			case '-':
				goeOper(character, 1);
				break;
			case '*':
			case '/':
				goeOper(character, 2);
				break;
			case '(':
				theStackChar.push(character);
				break;
			case ')':
				gotParen(character);
				break;
			default:
				output = output + character;
				break;
			}
		}
		while (!theStackChar.isEmpty()) {
			theStackChar.displayStack("While ");
			output = output + theStackChar.pop();
		}
		theStackChar.displayStack("End ");
		return output;
	}

	public void goeOper(char opThis, int prec1) {
		while (!theStackChar.isEmpty()) {
			char opTop = theStackChar.pop();
			if (opTop == '(') {
				theStackChar.push(opTop);
				break;
			} else {
				int prec2;
				if (opTop == '+' || opTop == '-') {
					prec2 = 1;
				} else {
					prec2 = 2;
				}
				if (prec2 < prec1) {
					theStackChar.push(opTop);
					break;
				} else {
					output = output + opTop;
				}
			}
		}
		theStackChar.push(opThis);
	}

	public void gotParen(char character) {
		while (!theStackChar.isEmpty()) {
			char chx = theStackChar.pop();
			if (chx == '(') {
				break;
			} else {
				output = output + chx;
			}
		}
	}
}

public class InfixToPostfix {
	public static void main(String[] args) throws IOException {
		String input;
		String output;
		while (true) {
			System.out.print("Enter infix: ");
			System.out.flush();
			input = getString();
			if (input.equals("")) {
				break;
			}

			InToPost theTrans = new InToPost(input);
			output = theTrans.doTrans();
			System.out.println("Postfix is " + output + '\n');
		}
	}

	public static String getString() throws IOException {
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		String string = br.readLine();
		return string;
	}
}
