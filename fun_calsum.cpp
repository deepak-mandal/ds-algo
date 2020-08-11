#include<iostream>
using namespace std;
float calsum(float x, float y, float z);
main()
{
float a, b, c;
cout<<"enter value of a, b, and c respectively : ";
cin>>a>>b>>c;
float sum = calsum(a, b, c);
cout<<"sum = "<<sum<<endl;

}
float calsum(float x, float y, float z)
{
float d;
d = x+y+z;
//return (d);
}
