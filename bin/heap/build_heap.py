def build_heap_top_down(a, n):
	for i in range(2, n+1):
		restore_up(i, a)
		
		
def restore_up(i, a):
	k=a[i]
	iparent=i//2
	while a[iparent] < k:
		a[i] = a[iparent]
		i=iparent
		iparent=i//2
	a[i]=k
	

######################################

a2=[99999, 20, 30, 15, 6, 40, 60, 45, 16, 75, 10, 80, 12]
n2=len(a2)-1

build_heap_top_down(a2, n2)
for i in range(1, n2+1):
	print(a2[i], ' ', end='')
print()
