#include<iostream>
using namespace std;
//Class declearation
class rectangle{
public:
double length;
double breadth;
double area(double length, double breadth);
};

main()
{
//Object declearation
rectangle rectangle1;
rectangle rectangle2;

rectangle1.length = 10;		//rectangle1 specification
rectangle1.breadth = 7;

//rectangle2 Specification
rectangle2.length = 5;
rectangle2.breadth = 7;

//double area = rectangle1.length*rectangle1.breadth;
cout<<"area of rectangle1 = "<<area()<<endl;

//area = rectangle2.length*rectangle2.breadth;
cout<<"area of rectangle2 = "<<area<<endl;


}
