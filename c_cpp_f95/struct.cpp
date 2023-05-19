#include <iostream>
using namespace std;
main()
{
struct book{
char name;
float price;
int page;
};

struct book b1, b2, b3;
cout<<"Enter name of book, price and no. of pages of book :\n";
cin>>b1.name>>b1.price>>b1.page;
cout<<"ENter name, price, page of the book\n";
cin>>b2.name>>b2.price>>b2.page;
cout<<"Again enter another date      :";
cin>>b3.name>>b3.price>>b3.page;

cout<<"Here see what you have entered :\n";
cout<<"name = "<<b1.name<<"	;"<<"price = "<<b1.price<<"	;"<<"no.of page = "<<b1.page<<endl;
cout<<"name = "<<b2.name<<"	;"<<"price = "<<b2.price<<"	;"<<"no. of page= "<<b2.page<<endl;
cout<<"name = "<<b3.name<<"	;"<<"price = "<<b3.price<<"	;"<<"no.of page = "<<b3.page<<endl;

}
