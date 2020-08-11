M = 1 
write (*,*) 'Please input number of runs'
read(*,*) knt

100	write (*,*) 'Please input two real number'
	read (*,*) a, b
M = M+1
c = a*b
d = a/b
e = a**b
write (*,*)'a = ',a,'b = ',b,'c = ',c,'d = ',d,'e = ',e
if (M .le.knt) go to 100
stop
end
