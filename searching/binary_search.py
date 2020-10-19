def binary_search(a, n, searchValue):
	first=0
	last=n-1
	
	while first<=last:
		mid=(first+last)//2
		if searchValue<a[mid]:
			last=mid-1	#search in left half
		elif searchValue>a[mid]:
			first=mid+1	#search in right half
		else:
			return mid	#searchValue present at index mid
	return -1
	
##########################################
n=int(input('Enter the number of elements: '))
a=[None]*n
print('Enter the element in sorted order - ')
for i in range(n):
	a[i] = int(input('Enter element: '))
searchValue = int(input('Enter the search value: '))

index=binary_search(a, n, searchValue)
if index == -1:
	print('value', searchValue, 'not present in the list')
else:
	print('value', searchValue, 'present at index ', index)
	
