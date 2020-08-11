#include <stdio.h>
#include <math.h>
int main()
{
	float num, root;
	printf("Enter a number: ");
	scanf("%f", &num);
	
	root = pow (num, 1/2.0);
	printf("Square root of %.2f = %.2f", num, root);
	return 0;
}
