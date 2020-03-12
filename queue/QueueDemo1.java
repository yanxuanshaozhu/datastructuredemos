package pers.yanxuanshaozhu.datastructure.queue;

class QueueWithCounter {
	private int maxSize;
	private int[] queArray;
	private int front;
	private int rear;
	private int nItems;

	public QueueWithCounter(int size) {
		maxSize = size;
		queArray = new int[maxSize];
		front = 0;
		rear = -1;
		nItems = 0;
	}

	public void insert(int value) {
		if (rear == maxSize - 1) {
			rear = -1;
		}
		queArray[++rear] = value;
		nItems++;
	}

	public int remove() {
		int temp = queArray[front++];
		if (front == maxSize - 1) {
			front = 0;
		}
		nItems--;
		return temp;
	}

	public int peek() {
		return queArray[front];
	}

	public boolean isEmpty() {
		return nItems == 0;
	}

	public boolean isFull() {
		return nItems == maxSize;
	}

	public int size() {
		return nItems;
	}

}

public class QueueDemo1 {
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
