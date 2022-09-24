#include <iostream>
using namespace std;
int main()
{
float a11, a12, a13, a21, a22, a23, a31, a32, a33, b1, b2, b3;
float l11, l12, l13, l21, l22, l23, l31, l32, l33, u11, u12, u13, u21, u22, u23, u31, u32, u33;
float y1, y2, y3, x, y, z;

cout<<"Enter the element of first linear equation as [A|B]\n";
cin>>a11>>a12>>a13>>b1;
cout<<"Enter the element of Second linear equation as [A|B]\n";
cin>>a21>>a22>>a23>>b2;
cout<<"Enter the element of Third linear equation as [A|B]\n";
cin>>a31>>a32>>a33>>b3;

l11 = 1; l12 = 0; l13 = 0; l22 = 1; l23 = 0; l33 = 1; u21 = 0; u31 = 0; u32 = 0;

u11 = a11; u12 = a12; u13 = a13; 
l21 = a21/u11;
u22 = a22 - u12*l21;
u23 = a23 - l21*u13;
l31 = a31/u11;
l32 = (a32 - l31*u12)/u22;
u33 = a33-l31*u13-l32*u23;

printf("\n");
printf("\n");

cout<<" the element of matrix L can be written as \n";
printf("%0.3f	%0.3f	%0.3f\n",l11, l12, l13);
printf("%0.3f	%0.3f	%0.3f\n",l21, l22, l23);
printf("%0.3f	%0.3f	%0.3f\n",l31, l32, l33);

printf("\n");
printf("\n");

cout<<"the element of matrix of U can be written as \n";
printf("%0.3f	%0.3f	%0.3f\n",u11, u12, u13);
printf("%0.3f	%0.3f	%0.3f\n",u21, u22, u23);
printf("%0.3f	%0.3f	%0.3f\n",u31, u32, u33);


y1 = b1;
y2 = b2 - l21*y1;
y3 = b3 - l31*y1 - l32*y2;

z = y3/u33;
y = (y2 - u23*z)/u22;
x = (y1 - u12*y - u13*z)/u11;


cout<<"\nOn solving the Equation UX = Y weget\n"<<endl;
cout<<" x = "<<x<<endl;
cout<<" y = "<<y<<endl;
cout<<" z = "<<z<<endl<<endl<<endl;

}
