#include <iostream>
using namespace std;

class rectangle			/* CLASS */
{
public : 
float length;		//length of a rectangle
float breadth;		//Breadth of a rectangle
};

int main()
{
rectangle rectangle1;		/* OBJECT car */	//Declared rectangle1 of type rectangle
rectangle rectangle2;		//Declared rectangle2 of type rectangle
float area = 0.0;		//store the area of a rectangle here
//rectangle1 specification
rectangle1.length = 6.0;
rectangle1.breadth = 7.0;
//rectangle2 specification
rectangle2.length = 5.0;
rectangle2.breadth = 6.0;
//area of rectrangle 1
area = rectangle1.length*rectangle1.breadth;
cout<<"Area of Rectangle1 : "<<area<<endl;
//area of rectangle2
area = rectangle2.length*rectangle2.breadth;
cout<<"Area of Rectangle2 : "<<area<<endl;
return 0;
}
