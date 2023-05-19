#include<iostream>
using namespace std;
//creating class
class rectangle {
public:
double length;		//length of a rectangle
double breadth;		//breadth of a rectangle
//men=mber function declaration
double getArea(void);
void setlength(double len);
void setbreadth(double bre);

};

//member function definition
double rectangle :: getArea()
{
double d = length*breadth;
return d;
}
void rectangle :: setlength(double len)
{
length = len;
}
void rectangle :: setbreadth(double bre)
{
breadth = bre;
}

main()
{
//creating object
rectangle rectangle1;
rectangle rectangle2;
double area = 0.0;

//rectangle1 Specification
rectangle1.setlength(12.0);
rectangle1.setbreadth(55.0);

//rectangle2 Specification
rectangle2.setlength(13.0);
rectangle2.setbreadth(5.0);

//area calculation
area = rectangle1.getArea();
cout<<"Area of rectangle1 = "<<area<<endl;

area = rectangle2.getArea();
cout<<"Area of rectangle2 = "<<area<<endl;

}
