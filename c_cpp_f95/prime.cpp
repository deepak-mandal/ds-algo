#include<iostream>
using namespace std;
main()
{
int n, i;
cout<<"Enter any number"<<endl;
cin>>n;

for(i = 1; i<=n; i++)
{
	if(n%i == 0)
	{
	cout<<"n = "<<n<<" is a prime number\n";
	}
	break;
	{
	cout<<"n = "<<n<<" is not a prime number\n";
	}
	
}


}
