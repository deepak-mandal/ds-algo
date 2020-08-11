#include<iostream>
using namespace std;

class rectangle{
public:
double length;		//length of a rectangle
double breadth;		//breadth of a rectangle
//Member function declaration
double getarea(void);
void setlength(double len);
void setbreadth(double bre);
};

//Member function definitions
double rectangle :: getarea(void)
{
return length*breadth;
}

void rectangle :: setlength(double len)
{
length = len;
}

void rectangle :: setbreadth(double bre)
{
breadth = bre;
}

//Main function for the program
main()
{
rectangle rectangle1;
rectangle rectangle2;
double area = 0.0;

//rectangle1 specification
rectangle1.setlength(12.0);
rectangle1.setbreadth(5.0);

//rectangle 2 specification
rectangle2.setlength(10.0);
rectangle2.setbreadth(12.0);

//area of rectangle1 
area = rectangle1.getarea();
cout<<"Area of rectangle1 : "<<area<<endl;
//area of reactangle2
area = rectangle2.getarea();
cout<<"Area of rectangle : "<<area<<endl;

}
