#include <stdio.h>
int main ()
{
int a;
int *p;
a = 5;
p = &a;
*p = 10;
printf ("%d\n",a);
printf ("%p\n",p);
printf ("%p\n",&a);
printf ("%d\n",*p);



return 0;
}
