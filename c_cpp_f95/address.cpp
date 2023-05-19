#include<iostream>
using namespace std;
main()
{
int arr[] = {1, 2, 3, 4, 5, 6};
int i = 0;
int *j;

for(i=0; i<6; i++)
{
j = &arr[i];
cout<<"Address of arr["<<i<<"] = "<<&arr[i]<<endl;
cout<<"value of arr["<<i<<"] = "<<*j<<endl;
}
}
