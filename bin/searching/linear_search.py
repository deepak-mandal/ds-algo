def search(a, n, searchValue):
	for i in range(n):
		if a[i] == searchValue:
			return i
	return -1
	
##########################################
n=int(input('Enter the number of elements: '))
a=[None]*n
print('Enter the element - ')
for i in range(n):
	a[i] = int(input('Enter element: '))
searchValue = int(input('Enter the search value: '))
index=search(a, n, searchValue)
if index == -1:
	print('value', searchValue, 'not present in the list')
else:
	print('value', searchValue, 'present at index ', index)
	
