#include<iostream>
using namespace std;
main()
{
//struct book{
char  name[3];
float price[3];
int page[3], i;
//};
 
//int i;
for(i=1; i<=3; i++)
{
cout<<"Enter name, price, page of the book:\n";
cin>>name[i]>>price[i]>>page[i];
}

cout<<"See Here what you have entered:\n";
for(i=1; i<=3; i++)
{
cout<<name[i]<<"	;"<<price[i]<<"		;"<<page[i]<<endl;
}


}
