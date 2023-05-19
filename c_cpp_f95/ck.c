#include <stdio.h>
int main()
{
// declare variables
char inst[100]; /*This is how you declare a string variable. In this string 100 characters is the
maximum capacity of the variable*/
char pnm [100]; // similarly as above
int tel;
int estyr;
// Accept values
printf("Enter institution's name :\n");
scanf (" %s", inst);
printf("Enter principal's name :\n");
scanf (" %s", pnm);
printf("Enter telephone number : \n");
scanf (" %d", &tel);
printf("Enter established year :\n");
scanf (" %d", &estyr);
// Print values
printf("Institution's name : %s \n", inst);
printf("Principal's name : %s \n", pnm);
printf("Telephone number : %d \n", tel);
printf("Established year : %d \n", estyr);
return 0;
}
