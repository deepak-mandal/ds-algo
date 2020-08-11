M = 0
100	write (*,*) 'Enter the value of a and b respectivilt'
	read (*,*) a, b
M = M+1
c = a*b
d = a/b
e = a**b
write (*,*)'a = ',a,'b = ',b, 'c = ',c,'d = ',d,'e = ',e

if (M .lt.10) go to 100
stop
end
