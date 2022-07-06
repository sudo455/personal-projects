#include "Element.hpp"

using namespace std;
using namespace Element;

Element(){}
Element(int an, string n, string s, double am){

    a_num=an;
    a_mass=am;
    name=n;
    symbol=s;
}

int get_num(){
    return a_num;
}

string get_name(){
    return name;
}

string get_symbol(){
    return symbol
}

double get_a_mass(){
    a_mass
}