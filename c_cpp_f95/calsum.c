#include <stdio.h>
int calsum (int x, int y, int z);
int main()
{
	int a, b, c, sum;
	printf ("Enter any three numbers\n");
	scanf ("%d %d %d\n",&a, &b, &c);
	sum = calsum (a, b, c);
	printf ("Sum = %d\n",sum);

	return (0);
}
	int calsum (int x, int y, int z)
	{
	int sum;
	sum = x + y + z;
	return (sum);
}
