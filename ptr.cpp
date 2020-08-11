#include<iostream>
using namespace std;
main()
{
/*char name1[15] = "Deepak";
char name2[15];*/
char *ptr1, *ptr2;
*ptr1 = "Mandal";
/*name2[15] = name1[15];
cout<<name2<<endl;*/
ptr2 = ptr1;
cout<<*ptr2<<endl;


}
