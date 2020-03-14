package pers.yanxuanshaozhu.datastructure.priorityqueue;

class PriorityQueue {
	private int maxSize;
	private int[] queArray;
	private int nItems;

	public PriorityQueue(int size) {
		maxSize = size;
		queArray = new int[maxSize];
		nItems = 0;
	}

	public void insert(int item) {
		int j;
		if (nItems == 0) {
			queArray[nItems++] = item;
		} else {
			for (j = nItems - 1; j >= 0; j--) {
				if (item > queArray[j]) {
					queArray[j + 1] = queArray[j];
				} else {
					break;
				}
			}
			queArray[j + 1] = item;
			nItems++;
		}
	}

	public int remove() {
		return queArray[--nItems];
	}

	public int peekMin() {
		return queArray[nItems - 1];
	}

	public boolean isEmpty() {
		return nItems == 0;
	}

	public boolean isFull() {
		return nItems == maxSize;
	}
}

public class PriorityQueueDemo {
	public static void main(String[] args) {
		PriorityQueue priorityQueue = new PriorityQueue(5);
		System.out.println("The sequence inserting elements into the priority queue:");
		System.out.println(30 + " " + 50 + " " + 10 + " " + 40 + " " + 20);
		priorityQueue.insert(30);
		priorityQueue.insert(50);
		priorityQueue.insert(10);
		priorityQueue.insert(40);
		priorityQueue.insert(20);
		System.out.println();
		System.out.println("The sequence ranking the elements from the front to the rear in the priority queue:");
		while (!priorityQueue.isEmpty()) {
			int item = priorityQueue.remove();
			System.out.print(item + " ");
		}

		System.out.println();
	}

}
