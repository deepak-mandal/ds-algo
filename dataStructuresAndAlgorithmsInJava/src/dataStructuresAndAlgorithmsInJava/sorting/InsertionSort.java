package dataStructuresAndAlgorithmsInJava.sorting;

import java.util.Arrays;

public class InsertionSort {

	private static void swap(int[] list, int iIndex, int jIndex) {
		int temp = list[iIndex];
		list[iIndex] = list[jIndex];
		list[jIndex] = temp;
	}

	public static void insertionSort(int[] listToSort) {
		for (int i = 0; i < listToSort.length - 1; i++) {
			System.out.println("\ni= " + i);
			for (int j = i + 1; j > 0; j--) {
				if (listToSort[j] < listToSort[j - 1]) {
					swap(listToSort, j, j - 1);
					System.out.println("swapping: " + j + " and " + (j - 1) + " ");
					System.out.println(Arrays.toString(listToSort));
				} else {
					break;
				}
			}
		}
	}

	public static void main(String[] args) {
		int unSortedList[] = new int[] { 40, 50, 60, 20, 10, 70, 100, 30, 80, 90 };
		System.out.println(Arrays.toString(unSortedList));
		insertionSort(unSortedList);
	}

}
