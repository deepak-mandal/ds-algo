#include <iostream>
using namespace std;
#include <math.h>
int main()
{

float x = -10.01, y = 10, z = 0;

printf("raising power of x to 3 : ");
printf("%f\n", pow(x, 3));
printf("square root of x : ");
printf("%f\n", sqrt(x));
printf("square root of x : ");
printf("%f\n", pow(x, 1/2.0));
printf("cube root of x : ");
printf("%f\n", pow(x, 1/3.0));
printf("Natural(base e) Log value of x : ");
printf("%f\n", log(x));
printf("Log base 10 of x : %f\n", log10(x));
printf("sin of x : ");
printf("%f\n", sin(x));
printf("Cosec of x : %f\n", 1/sin(x));
printf("Cos of x : %f\n", cos(x));
printf("Tan of x : %f\n", tan(x));
printf("acos of x : %f\n", acos(x));
printf("atan of x : %f\n", atan(x));
printf("inverse of sin of x : ");
printf("%f\n", asin(x));
printf("Absolute of x : %f\n",abs(x));
printf("Exponent raised to the x : ");
printf("%f\n", exp(x));

return 0;
}
