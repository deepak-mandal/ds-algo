#include<iostream>
#include<math.h>
using namespace std;
float dist(struct point pt1, struct point pt2);
main()
{
struct point{
float x;
float y;
};

struct point pt = {4, 3}, og = {0,0};
float d = dist(point pt, point og)
cout<<"Distance = "<<d<<endl;
}
float dist(struct point pt1, struct point pt2)
{
float d;
d = sqrt((pt1.x-pt2.x)*(pt1.x-pt2.x)+(pt1.y-pt2.y)*(pt1.y-pt2.y));
return d;
}
