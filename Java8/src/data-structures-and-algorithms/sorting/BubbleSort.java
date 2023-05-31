package dataStructuresAndAlgorithmsInJava.sorting;

import java.util.Arrays;

public class BubbleSort {

	public static void swap(int[] list, int iIndex, int jIndex) {
		int temp = list[iIndex];
		list[iIndex] = list[jIndex];
		list[jIndex] = temp;
	}

	public static void bubbleSort(int[] listToSort) {
		for (int i = listToSort.length - 1; i > 0; i--) {
			boolean swapped = false;
			System.out.println("\n i= " + i);
			for (int j = 0; j < i; j++) {
				if (listToSort[j] > listToSort[j + 1]) {
					swap(listToSort, j, j + 1);
					swapped = true;
					System.out.println("Swapping: " + j + " and " + (j + 1) + " ");
					System.out.println(Arrays.toString(listToSort));
				}
			}
			if (!swapped) {
				break;
			}
		}
	}

	public static void main(String[] args) {
		int unSortedList[] = new int[] { 42, 562, 214, 6853, 5, 53, 0, 356, 514, 1, 2, 55 };
		System.out.println(Arrays.toString(unSortedList));
		bubbleSort(unSortedList);
	}
	
}
