#include<iostream>
using namespace std;
main()
{
int arr[] = {10,20,30,40,50,60,75,85};
int *i, *j;
i = &arr[1];
j = &arr[0];
cout<<j<<"   "<<i<<endl;
cout<<"j-i = "<<j-i<<endl;
cout<<"*j-*i = "<<*j-*i<<endl;

}
