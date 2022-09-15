package io.github.deepakmandal;

import java.util.Arrays;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import io.github.deepakmandal.sorting.SelectionSort;

@SpringBootApplication
public class DsAlgoJavaApplication {

	public static void main(String[] args) {
		SpringApplication.run(DsAlgoJavaApplication.class, args);
		System.out.println("Data structure and algorithms in Java");
		
		SelectionSortAlgorithm();
		
		
		
	}

	private static void SelectionSortAlgorithm() {
		
		int unSortedList[] = new int[] {40, 50, 6, 2, 95, 1001, 565};
		System.out.println(Arrays.toString(unSortedList));
		SelectionSort selectionSort = new SelectionSort();
		selectionSort.selectionSort(unSortedList);
		
	}
	
	
	

}
