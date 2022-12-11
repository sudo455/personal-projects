#include <iostream>

using namespace std;

void p_line();
void p_line(char char_to_prnt);
void p_line(char char_to_prnt, int number1);
void p_line(char char_to_prnt1, char char_to_prnt2, int number1);

int main() {

    p_line();
    p_line('*');
    p_line('+', 15);
    p_line('+', '-', 30);

    return 0;
}

void p_line(){

    for(int i = 0; i < 15; i++){
        cout << "-";
    }
    cout << endl;
}
void p_line(char char_to_prnt){

    for(int i = 0; i < 15; i++){
        cout << char_to_prnt;
    }
    cout << endl;
    
}
void p_line(char char_to_prnt, int number1){

    for(int i = 0; i < number1; i++){
        cout << char_to_prnt;
    }
    cout << endl;

}
void p_line(char char_to_prnt1, char char_to_prnt2, int number1){

    for(int i = 0; i < number1; i++){
        cout << char_to_prnt1 << char_to_prnt2;
    }
    cout << endl;
    
}