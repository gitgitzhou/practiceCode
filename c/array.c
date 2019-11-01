#include <stdio.h> 

struct myStruct{
    int hight;
    int n[10];
};

int main()
{

int ix;
short myArray[]= { 3, 6, 9, 12, 15 };

struct myStruct hh; 
hh.hight = 10;
printf("%d\n", hh.hight);

struct myStruct *pstruct;
pstruct = &hh;
pstruct->hight = 20;
printf("%d\n", pstruct->hight);

/* printf("%d", pstruct->) */
for (ix=0; ix< (sizeof(myArray)/sizeof(short)); ++ix) 
{
  printf("%d", myArray[ix] );
}

}
