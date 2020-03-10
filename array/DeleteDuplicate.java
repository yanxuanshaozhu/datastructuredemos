package pers.yanxuanshaozhu.datastructure.array;

public class DeleteDuplicate {
	public static void main(String[] args) {
		int count = 0;
		int[] array = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
		for (int i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");

		}
		System.out.println();

		for (int i = 0; i < array.length; i++) {
			for (int j = i + 1; j < array.length; j++) {
				if (array[j] != array[i]) {
					array[i + 1] = array[j];
					count++;
					break;
				}

			}
		}
		System.out.println(count);
		if (array[array.length - 1] != array[count - 1]) {
			count++;
		}

		for (int i = 0; i < count; i++) {
			System.out.print(array[i] + " ");

		}
	}
}
