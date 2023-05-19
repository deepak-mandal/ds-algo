#include <iostream>
using namespace std;
main()
{
int a=0;
int n;
int j = 1, i = 1;
cout<<"enter n : ";
cin>>n;
for (i = 1; i<= n; i++)
{
	for(j = 1; j<=n; j++)
	{
	a = i+j;
	a = a-1;
cout<<a<<endl;
	}
}
cout<<a<<endl;

}
