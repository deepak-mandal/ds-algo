#include<stdio.h>
int main()
{
	int x = 5, y = 2, n;

n = 0;
while (x<y && x<0)
{
    x = x-y;
    n = n+1;
}
printf("Quotient value for %d by %d is %d\n",x, y, n);

    return 0;
}
