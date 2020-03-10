package pers.yanxuanshaozhu.datastructure.array;

public class ArrayDelete {
	public static void main(String[] args) {


		int[] array = new int[10];

		int target = 4;

		for (int i = 0; i < array.length; i++) {
			array[i] = (int) (Math.random() * 6);
		}

		for (int n : array) {
			System.out.print(n + " ");
		}
		System.out.println();


		int i;
		for (i = 0; i < array.length; i++) {
			if (array[i] == target) {
				break;
			}
		}

		for (int j = i; j < array.length - 1; j++) {
			array[j] = array[j + 1];
		}

		if (i == array.length) {
			System.out.println("Cannot find " + target);
		}

		else {
			for (int k = 0; k < array.length - 1; k++) {
				System.out.print(array[k] + " ");
			}
			System.out.println();
		}

	}
}
