#include <iostream>
#include <math.h>
float cube(float x);
int main()
{
float x, n;
printf("Enter a number for which you want to cube\n");
scanf("%f", &x);

n = cube(x);
printf("Cube of %f is given by %f\n", x, n);



return 0;
}
float cube(float x)
{
float d = pow(x, 3);

return (d);
}
