def quick_sort(a):
	sort(a, 0, len(a)-1)
	
def sort(a, low, up):
	if low>=up:
		return
	p=partition(a, low, up)
	sort(a, low, p-1)	#sort left sublist
	sort(a, p+1, up)
	
def partition(a, low, up):
	pivot=a[low]
	i=low+1	#move from lwft to right
	j=up	#move from right to left
	
	while i<=j:
		while a[i] < pivot and i < up:
			i+=1
		while a[j] > pivot:
			j-=1
		if i<j:	#swap
			temp=a[i]
			a[i]=a[j]
			a[j]=temp
			i+=1
			j-=1
		else:	#found proper place for pivot
			break
	#proper place for pivot is j
	a[low] = a[j]
	a[j] = pivot
	return j
	
	
###################################################

list1=[6, 3, 1, 5, 9, 8]
quick_sort(list1)
print(list1)

list2=[2, 3, 5, 39, 11, 8, 9, 166, 45, 23]
quick_sort(list2)
print(list2)

list3=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quick_sort(list3)
print(list3)

list4=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
quick_sort(list4)
print(list4)


list5=[4]
quick_sort(list5)
print(list5)
