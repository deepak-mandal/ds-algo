#include <iostream>
using namespace std;
main()
{
int i;
int mark[10];
int sum=0;
cout<<"enter marks of ten student"<<endl;

	for(i=1; i<11; i++)
	{
		cin>>mark[i];
		sum=sum+mark[i];
	}

float avmarks = sum/float(10);
cout<<"Avarage marks of 10 student = "<<avmarks<<endl;

}
