#include<iostream>
using namespace std;
main()
{
int i = 3, *x;
float j = 1.5, *y;
char k = 'c', *z;

cout<<i<<endl;
cout<<j<<endl;
cout<<k<<endl;



cout<<"Original Address :\n"<<endl;
cout<<&i<<endl;
cout<<&j<<endl;
cout<<&k<<endl<<endl;

x = &i; y=&j; z=&k;
cout<<*x<<endl;
cout<<*y<<endl;
cout<<*z<<endl;

cout<<"New address\n";
cout<<x<<endl;
cout<<y<<endl;
cout<<z<<endl;


}
