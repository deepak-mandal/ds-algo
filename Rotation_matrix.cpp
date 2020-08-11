#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
float a11, a12, a21, a22, x, y, z;
float r11, r12, r21, r22;

cout<<"enter the element of matrix A[2*2]\n";
cin>>a11>>a12;
cout<<"enter the second row element of the matrix\n";
cin>>a21>>a22;

z = atan(2*a12/(a11-a22));
cout<<"thita = "<<z<<endl<<endl;
z = z/2.0;
cout<<"thita = "<<z<<endl<<endl;

x = sin(z);
y = cos(z);

r11 = y;
r12 = -x;
r21 = x;
r22 = y;

cout<<"The rotation matrix can be written as\n"<<endl<<endl;
cout<<r11<<"	"<<r12<<endl;
cout<<r21<<"	"<<r22<<endl;



}
