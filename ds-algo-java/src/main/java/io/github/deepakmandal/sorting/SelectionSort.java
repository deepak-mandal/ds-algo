package io.github.deepakmandal.sorting;

import java.util.Arrays;

public class SelectionSort {

	public static void swap(int[] list, int iIndex, int jIndex) {
		int temp=list[iIndex];
		list[iIndex]=list[jIndex];
		list[jIndex]=temp;
	}
	
	
	public static void selectionSort(int[] listToSort) {
		
		for(int i=0; i<listToSort.length; i++) {
			System.out.println("\ni= "+i);
			
			for(int j=i+1; j<listToSort.length; j++) {
				if(listToSort[i]>listToSort[j]) {
					swap(listToSort, i, j);
					System.out.println("Swapping: "+i+ " and "+j+ "");
					System.out.println(Arrays.toString(listToSort));
				}
			}
		}
	}
	
	
	

}
