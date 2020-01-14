package pers.yanxuanshaozhu.datastructure.arraysort;

public class InsertionSort {
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

		for (int i = 1; i < array.length; i++) {
			int temp = array[i];
			int j = i;
			while (j > 0 && array[j-1] > temp) {
				array[j] = array[j-1];
				--j;
			}
			array[j] = temp;
		}
		
		System.out.println("After Insertion Sort:");
		for (int n : array) {
			System.out.print(n + " ");
		}
	}
}
