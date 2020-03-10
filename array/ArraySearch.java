package pers.yanxuanshaozhu.datastructure.array;

public class ArraySearch {
	public static void main(String[] args) {


		int[] array = new int[10];
		int target = 4;
		for (int i = 0; i < array.length; i++) {
			array[i] = (int) (Math.random() * 6);
		}

		for (int i : array) {
			System.out.print(i + " ");
		}
		System.out.println();


		int i;
		for (i = 0; i < array.length; i++) {
			if (array[i] == target) {
				System.out.println("At index " + i + " we find " + target);
				break;
			}
		}
		if (i == array.length) {
			System.out.println("cannot find " + target);
		}

	}
}
