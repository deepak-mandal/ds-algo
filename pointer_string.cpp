#include<iostream>
using namespace std;
main()
{
char name[15] = "Deepak Mandal";
char *ptr;
ptr = name;
while(*ptr !=  '\0')
{
cout<<*ptr;
ptr++;

}
cout<<endl;
}
