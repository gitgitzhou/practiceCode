// The output of this program can be different 
// in different runs. Note that the program 
// prints address of a variable and a variable 
// can be assigned different address in different 
// runs. 
#include <stdio.h> 

int main() 
{ 
	int x; 
    int *ptr;
    
    x = 10;

    ptr = &x;

    *ptr = 5;

    /* print variables value */
    printf("%d\n", x);

	// Prints address of x 
	printf("%p\n", &x); 

	printf("%p\n", ptr); 


	return 0; 
} 

