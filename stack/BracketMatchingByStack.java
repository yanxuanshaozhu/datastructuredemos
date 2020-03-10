package pers.yanxuanshaozhu.datastructure.stack;

import java.util.Scanner;

class CheckBracket {
	private String input;

	public CheckBracket(String input) {
		this.input = input;
	}

	public void check() {
		CharStack stack = new CharStack(input.length());
		for (int i = 0; i < input.length(); i++) {
			char value1 = input.charAt(i);
			switch (value1) {
			case '(':
			case '[':
			case '{':
				stack.push(value1);
				break;
			case '}':
			case ']':
			case ')':
				if (!stack.isEmpty()) {
					char value2 = stack.pop();
					if (value1 == '}' && value2 != '{' || value1 == ']' && value2 != '['
							|| value1 == ')' && value2 != '(') {
						System.out.println("Error: " + value1 + " at " + i);
					}
				} else {
					System.out.println("Error: " + value1 + " at " + i);
				}
				break;
			}
		}
		if (!stack.isEmpty()) {
			System.out.println("Error: not enough right brackets!");
		}
	}
}

public class BracketMatchingByStack {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String string = scanner.next();
		scanner.close();
		CheckBracket checkBracket = new CheckBracket(string);
		checkBracket.check();

	}
}
