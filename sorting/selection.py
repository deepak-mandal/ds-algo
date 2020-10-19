def selection_sort(a):
	for i in range(len(a) - 1):
		minIndex=i
		for j in range(i+1, len(a)):
			if a[j] < a[minIndex]:
				minIndex=j
		if i != minIndex:
			a[i], a[minIndex] = a[minIndex], a[i]
			
################################################################
list1=[6, 3, 1, 5, 9, 8]
selection_sort(list1)
print(list1)

list2=[2, 3, 5, 39, 11, 8, 9, 166, 45, 23]
selection_sort(list2)
print(list2)

