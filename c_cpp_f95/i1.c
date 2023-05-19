#include <stdio.h>
int main()
{
int d, r = 0, n, t;
printf("Enter a number :");
scanf("%d", &n);
t = n;

while(n>0)
{
d = n%10;
r = r*10+d;
n = n/10;
}
printf("Reverse : %d\n",r);

if(t == r)
printf("The number is palindrome\n");
else
printf("The number is not palindrome\n");

return 0;
}

