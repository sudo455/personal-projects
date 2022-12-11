#include <stdio.h>

// A variable declaration with structure declaration.
struct Point
{
   int x, y;
} p1;  // The variable p1 is declared with 'Point'
  
  
// A variable declaration like basic data types
struct Point2
{
   int x, y;
}; 
  
int main()
{
   struct Point2 p1;  // The variable p1 is declared like a normal variable
   // other wise the p1 the p1 is ready to use(?)
}