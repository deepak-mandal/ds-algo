#include<iostream>
using namespace std;
main()
{
int i = 3, *j, **k;
j = &i;
k = &j;
cout<<"Address of i = "<<*k<<endl;
cout<<"Address of i = "<<&i<<endl;
cout<<"Address of i = "<<j<<endl;
cout<<"Value of i = "<<i<<endl;
cout<<"Value of i = "<<*j<<endl;
cout<<"Value of i = "<<*&i<<endl;
cout<<"value of i = "<<**k<<endl;
cout<<"value of j = "<<j<<endl;
cout<<"Value of k = "<<k<<endl;
cout<<"address of j = "<<k<<endl;
cout<<"address of j = "<<&j<<endl;
cout <<"address of k = "<<&k<<endl;

}
