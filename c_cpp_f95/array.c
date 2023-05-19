#include <stdio.h>
int main ()
{
int avg, sum = 0;
int i;
int marks[30];	//array declaration

for (i = 0; i<=29; i++)
{
	printf ("Enter marks\n");
	scanf ("%d",&marks[i]);		//store data in array
}
for (i = 0; i<=29; i++)
	sum = sum + marks[i];		//read data from an array
	avg = sum/30;
	printf ("Average marks = %d\n",avg);
printf ("marks[29] = %d\n",marks[0]);
return 0;
}
