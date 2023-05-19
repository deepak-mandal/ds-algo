#include <stdio.h>
int main()
{
int a;
a = 5;
int *pa;
pa = &a;
int **ppa;
ppa = &pa;
**ppa = 100;
int *b;
b = pa;

printf("%p",*b);



return 0;
}
