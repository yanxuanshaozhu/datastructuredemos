package pers.yanxuanshaozhu.datastructure.linkedlist;

/**
 * In this demo, you can insert at the first Node, delete at the first Node,
 * search for nodes with specific values, delete nodes with specific values and
 * display all nodes in the linkedlist.
 */

class Node2 {
	private int iData;
	private double dData;
	private Node2 nextNode;

	public Node2() {

	}

	public Node2(int iData, double dData) {
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

	public final Node2 getNextNode() {
		return nextNode;
	}

	public final void setNextNode(Node2 nextNode) {
		this.nextNode = nextNode;
	}

	public void displayNode() {
		System.out.print("{" + iData + dData + "} ");
	}
}

class LinkedList2 {
	private Node2 firsrtNode;

	public boolean isEmpty() {
		return firsrtNode == null;
	}

	public void InsertFirst(int iData, double dData) {
		Node2 newNode = new Node2(iData, dData);
		newNode.setNextNode(firsrtNode);
		firsrtNode = newNode;
	}

	public Node2 deleteFirst() {
		Node2 tempNode = firsrtNode;
		firsrtNode = firsrtNode.getNextNode();
		return tempNode;
	}

	public Node2 find(int key) {
		Node2 currentNode = firsrtNode;
		while (currentNode.getiData() != key) {
			if (currentNode.getNextNode() == null) {
				return null;
			} else {
				currentNode = currentNode.getNextNode();
			}
		}
		return currentNode;
	}

	public Node2 delete(int key) {
		Node2 currentNode = firsrtNode;
		Node2 previousNode = firsrtNode;
		while (currentNode.getiData() != key) {
			if (currentNode.getNextNode() == null) {
				return null;
			} else {
				previousNode = currentNode;
				currentNode = currentNode.getNextNode();
			}
		}
		if (currentNode == firsrtNode) {
			firsrtNode = firsrtNode.getNextNode();
		} else {
			previousNode.setNextNode(currentNode.getNextNode());
		}
		return currentNode;
	}

	public void displayLinkedList() {
		System.out.print("List(first->last): ");
		Node2 currentNode = firsrtNode;
		while (currentNode != null) {
			currentNode.displayNode();
			currentNode = currentNode.getNextNode();
		}
	}
}

public class LinkedListDemo2 {
	public static void main(String[] args) {
		LinkedList2 theLinkedList = new LinkedList2();
		theLinkedList.InsertFirst(22, 2.99);
		theLinkedList.InsertFirst(44, 4.99);
		theLinkedList.InsertFirst(66, 6.99);
		theLinkedList.InsertFirst(88, 8.99);

		theLinkedList.displayLinkedList();
		System.out.println();

		Node2 node1 = theLinkedList.find(44);
		if (node1 != null) {
			System.out.println("Found node with key " + node1.getiData());
		} else {
			System.out.println("Can't find such node.");
		}

		Node2 node2 = theLinkedList.delete(66);
		if (node2 != null) {
			System.out.println("Deleted node with key" + node2.getiData());
		} else {
			System.out.println("Can't delete such node.");
		}

		theLinkedList.displayLinkedList();
	}
}
