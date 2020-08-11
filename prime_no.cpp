#include<iostream>
using namespace std;
main()
{
int num, i;
cout<<"Enter a num\n";
cin>>num;
i = 2;
while(i<= num-1)
{
	if(num%i ==0)
	{
	cout<<"Not a prime number\n";
	break;

	}

i++;

}

if(i==num)
cout<<"Prime number\n";

}
