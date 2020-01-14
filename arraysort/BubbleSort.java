package pers.yanxuanshaozhu.datastructure.arraysort;

public class BubbleSort {
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
		 * The part array[i+1], array[i+2],...,array[array.length-1] has already been sorted.
		 */
		
		for (int i = array.length-1; i > 0; i--) {      
			for (int j = 0; j < i; j++) {
				if (array[j] > array[j + 1]) {
					int temp = array[j];
					array[j] = array[j + 1];
					array[j + 1] = temp;
				}
			}
		}
		System.out.println("After Bubble Sort:");
		for (int n : array) {
			System.out.print(n + " ");
		}
	
	}
}
