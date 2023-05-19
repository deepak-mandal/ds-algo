#include<iostream>
using namespace std;
main()
{
int i = 3;
int *j;
j = &i;

cout<<"Address of i = "<<&i<<endl;
cout<<"Address of i = "<<j<<endl;
cout<<"Address of j = "<<&j<<endl;
cout<<"Address of i = "<<*&j<<endl;
cout<<"Value of i = "<<i<<endl;
cout<<"Value of i = "<<*&i<<endl;
cout<<"Value of i = "<<*j<<endl;



}
