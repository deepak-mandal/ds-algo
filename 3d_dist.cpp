#include<iostream>
#include<math.h>
using namespace std;
main()
{
struct point{
double x;		//x co-ordinate
double y;	
double z; 		//y co-ordinate
};

struct point pt = {4, 3, 1};		//initialisation set x-coordinate of pt pt.x = 4; set y-coordinate of pt : pt.y=3;
struct point on = {0, 0, 0};

float d = sqrt((pt.x-on.x)*(pt.x-on.x)+(pt.y-on.y)*(pt.y-on.y)+(pt.z-on.z)*(pt.z-on.z));
cout<<"Distance = "<<d<<endl;

}
