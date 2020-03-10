package pers.yanxuanshaozhu.datastructure.stack;

public class StackDemoUsingUtil {
	public static void main(String[] args) {
		java.util.Stack<Integer> stack = new java.util.Stack<Integer>();

		for (int i = 0; i < 10; i++) {
			int value = (int) (Math.random() * 100);
			stack.push(Integer.valueOf(value));
		}

		// stack size
		System.out.println("Stack size:");
		System.out.println(stack.size());

		// the element in the top of the stack without popping the stack
		System.out.println("The top element:");
		System.out.println(stack.peek());

		/*
		 * search an element from top of the stack to its bottom, if it is in the stack,
		 * then returns stack.size()- location of the element if the element is not in
		 * the stack, return -1
		 */
		System.out.println("The distance of the top elemnt:");
		System.out.println(stack.search(stack.peek()));

		// show all elements in the stack while popping
		System.out.println("Elements in the stack:");
		while (!stack.empty()) {
			System.out.print(stack.pop() + " ");
		}
		System.out.println();
		// whether the stack is empty
		System.out.println("Is the stack empty:");
		System.out.println(stack.empty());

	}
}
