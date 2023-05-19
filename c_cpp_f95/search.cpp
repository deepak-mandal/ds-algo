#include<iostream>
using namespace std;
main()
{
int arr[5] = {2, 3, 4, 10, 40};
int x, i;

cout<<"Enter a number that you want to find\n";
cin>>x;
//int n = sizeof(arr)/sizeof(int);
//cout<<"n = "<<n<<endl;

for(i=0; i<5; i++)
{
	if(arr[i] == x)
	{
	cout<<"Number found"<<endl;
	//break;
	}
	else
	{
	cout<<"Number doesn't found"<<endl;	
	}
}



}
