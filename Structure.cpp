#include<iostream>
using namespace std;
main()
{
struct book{
char name[15];
float price;
int page;
};

struct book b1, b2, b3;

cout<<"Enter name, prices and no. of pages of 3 book\n";
cin>>b1.name>>b1.price>>b1.page;
cin>>b2.name>>b2.price>>b2.page;
cin>>b3.name>>b3.price>>b3.page;

cout<<"And this is what you entered\n";
cout<<b1.name<<"	;"<<b1.price<<"		;"<<b1.page<<endl;
cout<<b2.name<<"	;"<<b2.price<<"		;"<<b2.page<<endl;
cout<<b3.name<<"	;"<<b3.price<<"		;"<<b3.page<<endl;

}
