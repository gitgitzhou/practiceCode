/* One of the powerful functions of the CPP is the ability to */ 
/* simulate functions using parameterized macros. */

#include <stdio.h>
#define square(x) ((x) * (x))
#define MAX(x,y) ((x) > (y) ? (x) : (y))

int main(void) {
   printf("square is %d\n", square(10));  
   printf("Max between 20 and 10 is %d\n", MAX(10, 20));
   return 0;
}
