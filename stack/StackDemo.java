package pers.yanxuanshaozhu.datastructure.stack;

class Stack {
	private int maxSize;
	private long[] stackArray;
	private int top;

	public Stack(int size) {
		maxSize = size;
		stackArray = new long[maxSize];
		top = -1;
	}

	public void push(long i) {
		stackArray[++top] = i; // First move up the top index, then push one element i into the stack.
	}

	public long pop() {
		return stackArray[top--]; // First pop the top element out of the stack, then move down the top index.
	}

	public long peek() {
		return stackArray[top];
	}

	public boolean isEmpty() {
		return (top == -1);
	}

	public boolean isFull() {
		return (top == maxSize - 1);
	}
}

public class StackDemo {
	public static void main(String[] args) {
		Stack theStack = new Stack(10);
		System.out.println("Elemens in the stack in the order of push");
		while (!theStack.isFull()) {
			long value = (long) (Math.random() * 100);
			theStack.push(value);
			System.out.print(value + " ");
		}
		System.out.println();
		System.out.println("*****************************");
		System.out.println("Elemens in the stack in the order of pop");
		while (!theStack.isEmpty()) {
			long value = theStack.pop();
			System.out.print(value + " ");
		}
		System.out.println();

	}
}
