#include <stdio.h>
#include <stdlib.h>
// Program checking if a number is both divisible by 5 and 7 both
int main()
{
	
	int x;

	printf("Enter an integer number : \n");
scanf("%d", &x);

if((x%5 || x%7) == 0)
{
    printf("it is divisible by both 5 and 7\n");
}
else
{
    printf("it is not divisible by both 5 and 7\n");
}











return 0;

}
