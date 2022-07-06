#include <iostream>
#include <string>
#include "MyRandom.h"

using namespace std;

class Q_add{

    private:

        static MyRandom mr;
        int a,b;

    public:
        Q_add();
        Q_add(int m);
        void print_request() const;
        int get_Correct() const;

};