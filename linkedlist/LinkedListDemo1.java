package pers.yanxuanshaozhu.datastructure.linkedlist;

/**
 * In this demo, you can insert at the first Node, delete at the first Node and
 * display all Nodes in the linkedlist.
 */

class Node1 {
	private int iData;
	private double dData;
	private Node1 nextNode;

	public Node1() {

	}

	public Node1(int iData, double dData) {
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

	public final Node1 getNextNode() {
		return nextNode;
	}

	public final void setNextNode(Node1 nextNode) {
		this.nextNode = nextNode;
	}

	public void displayNode() {
		System.out.print("{" + iData + dData + "} ");
	}
}

class LinkedList1 {
	private Node1 firstNode;

	public boolean isEmpty() {
		return firstNode == null;
	}

	public void InsertFirst(int iData, double dData) {
		Node1 newNode = new Node1(iData, dData);
		newNode.setNextNode(firstNode);
		firstNode = newNode;
	}

	public Node1 deleteFirst() {
		Node1 tempNode = firstNode;
		firstNode = firstNode.getNextNode();
		return tempNode;
	}

	public void displayLinkedList() {
		System.out.print("List(first->last): ");
		Node1 currentNode = firstNode;
		while (currentNode != null) {
			currentNode.displayNode();
			currentNode = currentNode.getNextNode();
		}
	}
}

public class LinkedListDemo1 {
	public static void main(String[] args) {
		LinkedList1 theLinkedList = new LinkedList1();
		theLinkedList.InsertFirst(22, 2.99);
		theLinkedList.InsertFirst(44, 4.99);
		theLinkedList.InsertFirst(66, 6.99);
		theLinkedList.InsertFirst(88, 8.99);

		theLinkedList.displayLinkedList();
		System.out.println();

		while (!theLinkedList.isEmpty()) {
			Node1 aNode = theLinkedList.deleteFirst();
			System.out.print("Deleted ");
			aNode.displayNode();
			System.out.println();
		}
		theLinkedList.displayLinkedList();
	}
}
