#include <iostream>
using namespace std;
int main()
{
float a11, a12, a13, a21, a22, a23, a31, a32, a33, b11, b12, b13, b21, b22, b23, b31, b32, b33;


cout<<"Enter first row element of the matrix as [a]|[B]\n";
cin>>a11>>a12>>a13>>b11>>b12>>b13;
cout<<"Enter Second row element of the matrix as [a]|[B]\n";
cin>>a21>>a22>>a23>>b21>>b22>>b23;
cout<<"Enter third row element of the matrix as [a]|[B]\n";
cin>>a31>>a32>>a33>>b31>>b32>>b33;


cout<<endl<<endl<<endl;
cout<<a11<<"  "<<a12<<"  "<<a13<<"  "<<b11<<" "<<b12<<" "<<b13<<endl;
cout<<a21<<"  "<<a22<<"  "<<a23<<"  "<<b21<<" "<<b22<<" "<<b23<<endl;
cout<<a31<<"  "<<a32<<"  "<<a33<<"  "<<b31<<" "<<b32<<" "<<b33<<endl;
cout<<endl;

if(a11 != 0)
{
	a11 = a11/a11; a12 = a12/a11; a13 = a13/a11; b11 = b11/a11; b12 = b12/a11; b13 = b13/a11;
}
if(a21 != 0)
{
	a21 = a21/a21; a22 = a22/a21; a23 = a23/a21; b21 = b21/a21; b22 = b22/a21; b23 = b23/a21;
}
if(a31 != 0)
{
	a31 = a31/a31; a32 = a32/a31; a33 = a33/a31; b31 = b31/a31; b32 = b32/a31; b33 = b33/a31;
}
if(a21 != 0)
{
	a21 = a21-a11; a22 = a22-a12; a23 = a23-a13; b21 = b21-b11; b22 = b22-b12; b23 = b23-b13;
}
if(a31 != 0)
{
	a31 = a31-a11; a32 = a32-a12; a33 = a33-a13; b31 = b31-b11; b32 = b32-b12; b33 = b33-b13;
}

cout<<endl<<endl<<endl;
cout<<a11<<"  "<<a12<<"  "<<a13<<"  "<<b11<<" "<<b12<<" "<<b13<<endl;
cout<<a21<<"  "<<a22<<"  "<<a23<<"  "<<b21<<" "<<b22<<" "<<b23<<endl;
cout<<a31<<"  "<<a32<<"  "<<a33<<"  "<<b31<<" "<<b32<<" "<<b33<<endl;
cout<<endl;

cout<<endl;
cout<<endl;

if(a12 != 0)
{
a11 = a11/a12; a12 = a12/a12; a13 = a13/a12; b11 = b11/a12; b12 = b12/a12; b13 = b13/a12;
}
if(a22 != 0)
{
a21 = a21/a22; a22 = a22/a22; a23 = a23/a22; b21 = b21/a22; b22 = b22/a22; b23 = b23/a22;
}
if(a32 != 0)
{
a31 = a31/a32; a32 = a32/a32; a33 = a33/a32; b31 = b31/a32; b32 = b32/a32; b33 = b33/a32;
}

if(a11 != 0)
{
a11 = a11-a21; a12 = a12-a22; a13 = a13-a23; b11 = b11-b21; b12 = b12-b22; b13 = b13-b23;
}
if(a31 != 0)
{
a31 = a31-a21; a32 = a32-a22; a33 = a33-a23; b31 = b31-b21; b32 = b32-b22; b33 = b33-b23;
}

cout<<a11<<"  "<<a12<<"  "<<a13<<"  "<<b11<<" "<<b12<<" "<<b13<<endl;
cout<<a21<<"  "<<a22<<"  "<<a23<<"  "<<b21<<" "<<b22<<" "<<b23<<endl;
cout<<a31<<"  "<<a32<<"  "<<a33<<"  "<<b31<<" "<<b32<<" "<<b33<<endl;
cout<<endl;

cout<<endl<<endl;
cout<<endl;

if(a13 != 0)
{
a11 = a11/a13; a12 = a12/a13; a13 = a13/a13; b11 = b11/a13; b12 = b12/a13; b13 = b13/a13;
}
if(a23 != 0)
{a21 = a21/a23; a22 = a22/a23; a23 = a23/a23; b21 = b21/a23; b22 = b22/a23; b23 = b23/a23;
}
if(a33 != 0)
{
a31 = a31/a33; a32 = a32/a33; a33 = a33/a33; b31 = b31/a33; b32 = b32/a33; b33 = b33/a33;
}

if(a11 != 0)
{
a11 = a11-a31; a12 = a12-a32; a13 = a13-a33; b11 = b11-b31; b12 = b12-b32; b13 = b13-b33; 
}
if(a21 != 0)
{
a21 = a21-a31; a22 = a22-a32; a23 = a23-a33; b12 = b12-b31; b22 = b22-b32; b23 = b23-b33;
}


cout<<a11<<"  "<<a12<<"  "<<a13<<"  "<<b11<<" "<<b12<<" "<<b13<<endl;
cout<<a21<<"  "<<a22<<"  "<<a23<<"  "<<b21<<" "<<b22<<" "<<b23<<endl;
cout<<a31<<"  "<<a32<<"  "<<a33<<"  "<<b31<<" "<<b32<<" "<<b33<<endl;
cout<<endl;

cout<<endl<<endl<<endl;

if(a11 != 0)
{
a11 = a11/a11; a12 = a12/a11; a13 = a13/a11; b11 = b11/a11; b12 = b12/a11; b13 = b13/a11;
}
if(a22 != 0)
{
a21 = a21/a22; a22 = a22/a22; a23 = a23/a22; b22 = b22/a22; b22 = b22/a22; b23 = b23/a22;
}
if(a33 != 0)
{
a31 = a31/a33; a32 = a32/a33; a33 = a33/a33; b33 = b33/a33; b32 = b32/a33; b33 = b33/a33;
}


cout<<"The inverse of the matrix is :-"<<endl<<endl<<endl;
cout<<"  "<<b11<<" "<<b12<<" "<<b13<<endl;
cout<<"  "<<b21<<" "<<b22<<" "<<b23<<endl;
cout<<"  "<<b31<<" "<<b32<<" "<<b33<<endl;
cout<<endl;

//cout<<endl<<endl<<endl;
//cout<<"x = "<<b1<<endl;
//cout<<"y = "<<b2<<endl;
//cout<<"z = "<<b3<<endl;



}
