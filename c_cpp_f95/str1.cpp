#include<iostream>
#include<math.h>
using namespace std;
struct point{
int x;
int y;
};
float dist(struct point, struct point);
main()
{
struct point pt = {4, 3}, og = {0, 0};
cout<<"distance = "<<dist(pt, og);

}

float dist(struct point pt1, struct point pt2)
{
float d;
d = sqrt((pt1.x-pt2.x)*(pt1.x-pt2.x)+(pt1.y-pt2.y)*(pt1.y-pt2.y));
return d;
}
