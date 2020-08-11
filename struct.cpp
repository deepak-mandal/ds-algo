#include<iostream>
using namespace std;
main()
{
char name[3];
float price[3];
int page[3], i;

cout<<"Enter name, prices and no. of pages of 3 books\n";

for(i=0; i<=2; i++)
cin>>name[i]>>price[i]>>page[i];
cout<<"And this is what you Entered\n";
for(i=0; i<=2; i++)
cout<<name[i]<<price[i]<<page[i]<<endl;




}
