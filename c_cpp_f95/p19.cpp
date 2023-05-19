#include <iostream>
using namespace std;
int main()
{
int i = 3, *j, **k;
j = &i;
k = &j;

cout<<"Address of i = "<<&i<<endl;
cout<<"Address of i = "<<j<<endl;
cout<<"Address of i = "<<*k<<endl;
cout<<"Address of j = "<<&j<<endl;
cout<<"Address of j = "<<k<<endl;
cout<<"Address of k = "<<&k<<endl;
cout<<"Value of j = "<<j<<endl;
cout<<"Value of k = "<<k<<endl;
cout<<"Value of i = "<<i<<endl;
cout<<"Value of i = "<<*j<<endl;
cout<<"Value of i = "<<**k<<endl;
cout<<"Value of i = "<<*(&i)<<endl;

}
