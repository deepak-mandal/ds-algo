write (*,*)'Please input the number of runs'
read (*,*) knt
if (knt .gt. 10) then
write (*,*)'no more than 10 runs are allowed'
write (*,*)'please input an integer less than 11to continue or type o to quit'
read (*,*) knt
write (*,*) 'Number of runs = ',knt
if (knt .eq. 0)stop 

end if
M = 1 
100	write (*,*)'Please input two real number'
	read (*,*) a, b
M = M+1
c = a*b
d = a/b
e = a**b
write (*,*)'a = ',a,'b = ',b,'c = ',c,'d = ',d,'e = ',e
if (M.le.knt) goto 100

stop
end
