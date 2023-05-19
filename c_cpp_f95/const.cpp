#include<iostream>
using namespace std;
//creating class
class square{
public:
int side;
square();		//constructor declearation
};

square :: square()		//constructor definition using class square which doesn't have any return type
{
side = 20;
}

main()
{
//creating object
square c;
cout<<c.side<<endl;



}
