#include <iostream>
using namespace std;
int main()
{
float avg, sum = 0;
int i;
float marks[30];		//arry declearation

for(i=0; i<=29; i++)
{
cout<<"Enter mark\n";
cin>>marks[i];		//store data in array
}


for(i=0; i<=29; i++)
{
sum = sum + marks[i];

}

avg = sum/30.0;
cout<<"Sum = "<<sum<<endl<<"Average marks = "<<avg<<endl;




}
