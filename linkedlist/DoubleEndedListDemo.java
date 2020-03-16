package pers.yanxuanshaozhu.datastructure.linkedlist;

class Node3 {
	private int iData;
	private double dData;
	private Node3 nextNode;

	public Node3() {

	}

	public Node3(int iData, double dData) {
		this.iData = iData;
		this.dData = dData;
		this.nextNode = null;
	}

	public int getiData() {
		return iData;
	}

	public void setiData(int iData) {
		this.iData = iData;
	}

	public double getdData() {
		return dData;
	}

	public void setdData(double dData) {
		this.dData = dData;
	}

	public final Node3 getNextNode() {
		return nextNode;
	}

	public final void setNextNode(Node3 nextNode) {
		this.nextNode = nextNode;
	}

	public void displayNode() {
		System.out.print("{" + iData + dData + "} ");
	}
}

class FirstLastLink {
	private Node3 firstNode;
	private Node3 lastNode;

	public boolean isEmpty() {
		return firstNode == null;
	}

	public void InsertFirst(int iData, double dData) {
		Node3 newNode = new Node3(iData, dData);
		if (isEmpty()) {
			lastNode = newNode;
		}
		newNode.setNextNode(firstNode);
		firstNode = newNode;
	}

	public void InsertLast(int iData, double dData) {
		Node3 newNode = new Node3(iData, dData);
		if (isEmpty()) {
			firstNode = newNode;
		} else {
			lastNode.setNextNode(newNode);
		}
		lastNode = newNode;
	}

	public Node3 deleteFirst() {
		Node3 tempNode = firstNode;
		if (firstNode.getNextNode() == null) {
			lastNode = null;
		}
		firstNode = firstNode.getNextNode();
		return tempNode;
	}

	public void displayList() {
		System.out.print("List (first-->last): ");
		Node3 currentNode = firstNode;
		while (currentNode != null) {
			currentNode.displayNode();
			currentNode = currentNode.getNextNode();
		}
		System.out.println("");
	}
}

public class DoubleEndedListDemo {
	public static void main(String[] args) {
		FirstLastLink theFirstLastLink = new FirstLastLink();
		theFirstLastLink.InsertFirst(22, 2.99);
		theFirstLastLink.InsertFirst(44, 4.99);
		theFirstLastLink.InsertFirst(66, 6.99);
		theFirstLastLink.InsertLast(11, 1.99);
		theFirstLastLink.InsertLast(33, 3.99);
		theFirstLastLink.InsertLast(55, 5.99);

		theFirstLastLink.displayList();

		theFirstLastLink.deleteFirst();
		theFirstLastLink.deleteFirst();
		theFirstLastLink.displayList();
	}
}
