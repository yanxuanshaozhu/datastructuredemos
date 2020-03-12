package pers.yanxuanshaozhu.datastructure.queue;

class QueueWithoutCounter {
	private int maxSize;
	private int[] queArray;
	private int front;
	private int rear;

	public QueueWithoutCounter(int size) {
		maxSize = size + 1;
		queArray = new int[maxSize];
		front = 0;
		rear = -1;
	}

	public void insert(int val) {
		if (rear == maxSize) {
			rear = -1;
		}
		queArray[++rear] = val;
	}

	public int remove() {
		int temp = queArray[front++];
		if (front == maxSize) {
			front = 0;
		}
		return temp;
	}

	public int peek() {
		return queArray[front];
	}

	public boolean isEmpty() {
		return (rear + 1 == front || (front + maxSize - 1 == rear));
	}

	public boolean isFull() {
		return (rear + 2 == front || (front + maxSize - 2 == rear));
	}

	public int size() {
		if (rear >= front) {
			return rear - front + 1;
		} else {
			return (maxSize - front) + (rear + 1);
		}
	}
}

public class QueueDemo2 {
	public static void main(String[] args) {
		QueueWithCounter queue = new QueueWithCounter(5);

		queue.insert(10);
		queue.insert(20);
		queue.insert(30);
		queue.insert(40);

		queue.remove();
		queue.remove();
		queue.remove();

		queue.insert(50);
		queue.insert(60);
		queue.insert(70);
		queue.insert(80);

		while (!queue.isEmpty()) {
			int val = queue.remove();
			System.out.print(val);
			System.out.print(" ");
		}
		System.out.println();
	}
}
