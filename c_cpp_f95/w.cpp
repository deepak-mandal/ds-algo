#include <iostream>
using namespace std;
main()
{
int p, n, count;
float r, si;
count = 1;
while(count<=3)
{
cout<<"Enter value of p, n and r respectively : ";
cin>>p>>n>>r;
si = p*n*r/100;
cout<<"simple interest = Rs.% "<<si<<endl;
count = count +1;
}

}
