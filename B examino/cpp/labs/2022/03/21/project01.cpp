#include <iostream>
#include "Q_add.h"
 
using namespace std;

int main() {

    int score = 0, total = 0, answ;

    while(score < 3){
        Q_add q1(20);
        q1.print_request();
        cin >> answ;
        if (answ == q1.get_Correct()){

            cout << "correct " << endl;
            score++;

        }else{
            cout << "wrong input try again" << endl;
        }
        total++;
    }

    cout << "the correct answers is:" << score << endl << "total tries is:" << total << endl;

    return 0;
}