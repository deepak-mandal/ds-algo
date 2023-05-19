
write(*,*)'Enter the value of x and y respectevily'
read(*,*)x,y
 if (x<y) then
temp = x
x = y
y = temp
write (*,*) 'x = ',x,'y = ',y
end if 
stop
end
