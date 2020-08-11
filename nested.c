#include <stdio.h>
int main()
{
	int i, j, p = 1;

	for(i = 1; i <= 15; i++) // for number of rows
	{	
		for(j = i; j <= i; j++) // for columns
		{
		printf("%d ", p);
				p++;
	}
	printf("\n");
	}
	return 0;
}
