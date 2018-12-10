#include <stdio.h>

#define LENGTH 10   
#define WIDTH  5
#define NEWLINE '\n'

int main() {
   int area;  
  
   area = LENGTH * WIDTH;
   printf("value of area : %d", area);
   printf("%c", NEWLINE);

   const int  L = 10;
   const int  W = 5;
   const char N = '\n';
   
   area = L * W;
   printf("value of area : %d", area);
   printf("%c", N);

   return 0;

}
