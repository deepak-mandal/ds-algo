#include<iostream>
using namespace std;
main()
{
int arr[6] = {1,2,3,4,5,6};
int *a, *b;
a = &arr[4];
b = arr+4;

if(*a==*b)
{
cout<<"both a and b are same\n"; 
cout<<"a = "<<a<<endl;
cout<<"b = "<<b<<endl;
}
else
{
cout<<"both a and b are different\n";
cout<<"b = "<<b<<endl;
}
}
