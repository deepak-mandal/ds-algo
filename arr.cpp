#include <iostream>
using namespace std;
int main()
{
int arr[4], i,  sum;
cout<<"enter any four  number\n";

for(i = 0; i<4; i++)
{
cin>>arr[i];
}
sum = 0;
for(i=0; i<4; i++)
{
sum = sum + arr[i];
}
cout<<"sum = "<<sum<<endl;

}
