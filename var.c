#include <stdio.h>
#include <stdlib.h>
int main()
{
	// Variable declaration
	int i, j, p = 1;
	// Print Pattern
	for(i = 1; i <= 5; i++) // for number of rows
	{
		for(j = 1; j <= i; j++) // for columns
		{
			printf("%d ", p);
			p ++;
		}
		printf("\n");
	}

	return 0;
}
