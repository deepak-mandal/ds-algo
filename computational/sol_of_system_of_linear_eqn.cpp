#include <iostream>
using namespace std;
int main()
{

float a11, a12, a13, a21, a22, a23, a31, a32, a33, b1, b2, b3, x, y, z, y1, y2, y3;
float l21, l31, l32, u11, u12, u13, u22, u23, u33;


//LU Decomposition Method
cout<<"Enter the element of equation1\n";
cin>>a11>>a12>>a13>>b1;
cout<<"Enter the element of equation2\n";
cin>>a21>>a22>>a23>>b2;
cout<<"Enter the element of equation3\n";
cin>>a31>>a32>>a33>>b3;

//[A] = [L]*[U];

u11 = a11;
u12 = a12;
u13 = a13;
l21 = a21/u11;
u22 = a22-l21*u12;
u23 = a23-l21*u13;
l31 = a31/u11;
l32 = (a32-l31*u12)/u22;
u33 = a33-u13*l31-l32*u23;


cout<<endl;
cout<<endl;


cout<<"[L]*[U] = [A]\n";

cout<<endl;
cout<<endl;

cout<<" 1	"<<" 0	"<<"0	"<<"			"<<u11<<" "<<u12<<" "<<u13<<"			"<<a11<<" "<<a12<<" "<<a13<<endl;
cout<<l21<<" 1	"<<" 0	"<<"			"<<" 0	"<<u22<<" "<<u23<<" 		  	  =	"<<a21<<" "<<a22<<" "<<a23<<endl;
cout<<l31<<" "<<l32<<" 1	"<<"			"<<" 0	"<<" 0	"<<u33<<"				"<<a31<<" "<<a32<<" "<<a33<<endl;

cout<<endl;
cout<<endl;


cout<<"[L]*[Y] = [B]"<<endl;
y1 = b1;
y2 = b2-l21*y1;
y3 = b3-y2*l32-y1*l31;

cout<<endl;
cout<<endl;

cout<<"      "<<y1<<endl;
cout<<"[Y] = "<<y2<<endl;
cout<<"      "<<y3<<endl;


cout<<endl;
cout<<endl;


cout<<"[U]*[X] = [Y]\n";
z = y3/u33;
y = (y2-u23*z)/u22;
x = (y1-u13*z-u12*y)/u11;

cout<<endl;
cout<<endl;


cout<<"The Solution of System of linear equation is\n";
cout<<endl;
cout<<"      "<<x<<endl;
cout<<"[X] = "<<y<<endl;
cout<<"      "<<z<<endl;

}
