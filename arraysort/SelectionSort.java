package pers.yanxuanshaozhu.datastructure.arraysort;

public class SelectionSort {
	public static void main(String[] args) {

		int[] array = new int[10];

		for (int i = 0; i < array.length; i++) {
			array[i] = (int) (Math.random() * 100);
		}

		System.out.println("Initial Array:");
		for (int n : array) {
			System.out.print(n + " ");
		}
		System.out.println();
		
		/*
		 *  The part array[0],array[1],...,array[i]  has already been sorted.
		 */
		
		for (int i = 0; i < array.length - 1; i++) {
			int min = i;
			for (int j = i + 1; j < array.length; j++) {
				if (array[j] < array[min]) {
					min = j;
				}
			}
			int temp = array[i];
			array[i] = array[min];
			array[min] = temp;
		}
		System.out.println("After Selection Sort:");
		for (int n : array) {
			System.out.print(n + " ");
		}
		
	}
}
