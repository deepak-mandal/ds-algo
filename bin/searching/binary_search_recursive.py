def binary_search(a, n, searchValue):
	return _search(a, 0, n-1, searchValue)

def _search(a, first, last, searchValue):
	if (first>last):
		return -1	#search is unsuccessful
		
	mid=(first+last)//2
	if searchValue>a[mid]:	#search in right half
		return _search(a, mid+1, last, searchValue)
	elif searchValue < a[mid]:	#search in left half
		return _search(a, first, mid-1, searchValue)
	else: 
		return mid	#search is successful
	
	
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
	
