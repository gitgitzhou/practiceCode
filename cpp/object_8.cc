#include <iostream>
 
using namespace std;
class Line {
   public:
      void setLength( double len );
      double getLength( void );
      Line(double len);   // This is the constructor declaration
      ~Line();  // This is the destructor: declaration
 
   private:
      double length;
};
 
// Member functions definitions including constructor and destructor

Line::Line( double len ) : length(len) {
   cout << "Object is being created" << endl;
}

Line::~Line(void) {
   cout << "Object is being deleted" << endl;
}

void Line::setLength( double len ) {
   length = len;
}

double Line::getLength( void ) {
   return length;
}

// Main function for the program
double a;
int main() {

   Line line(10.0);
   a = 10; 
   // get initially set length.
   cout << "Initial length of line : " << line.getLength() << endl;

   // set line length
   line.setLength(6.0); 
   cout << "Length of line : " << line.getLength() << endl;
   cout << a << endl; 
   return 0;
}

