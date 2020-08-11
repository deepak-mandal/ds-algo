#include <stdio.h>
int main()
{
int n, d, r = 0, a, b;
a = 0, b = 0;

printf("Enter any number :\n");
scanf("%d", &n);

while(n>0)
{
d = n%10;
r = r*10+d;
n = n/10;

if(d%2 == 0)
a = a+1;
else
b = b+1;

}
 

printf("The counts of even digit in the number: %d\n", a);
printf("The counts of odd digit in the number : %d\n", b);



return 0;
}
