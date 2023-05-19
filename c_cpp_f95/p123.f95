real y(8), f(8)
open (unit = 1, file = 'eular.out', status = 'new')
y(0) = 0.5
h = 0.1

do 10 i = 0, 0.7, 0.1
f(i) = y(i) - i
y(i+h) = 0.0
y(i+h) = y(i+h) + y(i) + h*f(i)
write(1,*)' y(',i,'+0.1)', ' = ', y(i+h)
10 continue
stop
end

