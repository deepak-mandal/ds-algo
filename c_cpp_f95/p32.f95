
write(*,*)'Enter the value of n to calculate n!'
read (*,*)n
k1 = 1
do 10 k = 1,n
k1 = k*k1
10 continue
write (*,*)'n! = ',k1
stop
end

