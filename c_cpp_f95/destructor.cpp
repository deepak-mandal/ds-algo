#include<iostream>
using namespace std;
//creating class
class square{
public:
int side;
square();		//constructor declaration 
~square()		//destructor declaration
{
cout<<"Object has deleted"<<endl;
}

};
square :: square()
{
side = 20;
}

main()
{
//creating object
square c;
cout<<c.side<<endl;


}
