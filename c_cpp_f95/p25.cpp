#include <iostream>
using namespace std;
int calsum (int x, int y, int z);
int main()
{
int a, b, c, sum;
cout<<"Enter any three numbers\n";
cin>>a>>b>>c;
sum = calsum(a,b,c);
cout<<"Sum = "<<sum<<endl;

}
int calsum(int x, int y, int z)
{
int d;
d = x + y + z;
//return d;

}
