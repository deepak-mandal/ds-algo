#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{

float x, y, z;
cout<<"Enter any value of x(in degree) to calculate Sin(x)\n";
cin>>x;

//Calculation of PI
z = atan(1);
cout<<"tan^-1(1) = "<<z<<endl;
z = 4*atan(1);
cout<<"PI = "<<z<<endl;

x = x*z/180;
cout<<"x (in radian) = "<<x<<endl;
y = sin(x);

cout<<"Sin(x) = "<<y<<endl;


}
