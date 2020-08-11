#include <stdio.h>
int main()
{
    char ins[25], name[25], num[10];
    int etd;
    
    printf("Enter Institute name :\n");
    scanf("%s", ins);
    printf("Enter Your name :\n");
    scanf("%s", name);
    printf("Enter Phone number :\n");
    scanf("%s", num);
    printf("Enter  year of establishment :\n");
    scanf("%d", &etd);
    printf("\n");

    printf("Institute name : %s \n", ins);
    printf("Principal's name : %s \n", name);
    printf("Telephone no. : %s \n", num);
    printf("Year of establishment : %d \n",etd);
    
    return 0;
}
