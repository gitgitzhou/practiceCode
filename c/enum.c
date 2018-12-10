// An example program to demonstrate working 
// of enum in C 
#include<stdio.h> 
  
enum week{Mon, Tue, Wed, Thur, Fri, Sat, Sun}; 
  
enum year{Jan, Feb, Mar, Apr, May, Jun, Jul,
          Aug, Sep, Oct, Nov, Dec};

int main() 
{ 
    enum week day; 
    day = Wed; 
    printf("%d\n",day); 
    
    int i;
    for (i=Jan; i<=Dec; i++ )
        printf("%d ", i);

    return 0; 
} 
