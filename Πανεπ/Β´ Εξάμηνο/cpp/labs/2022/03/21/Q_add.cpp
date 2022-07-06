#include "Q_add.h"

Q_add::Q_add(int m){
    a= mr.get_number(m);
    b= mr.get_number(m);
}
void Q_add::print_request() const{
    cout << a << " + " << b << " = ";
}
int Q_add::get_Correct() const{
    return a+b;
}
MyRandom Q_add::mr;