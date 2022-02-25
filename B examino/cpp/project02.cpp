#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    
    double eyrdol = 1.144, eyryen = 131.541, eyrelvfrang = 1.053, eyrsterl = 0.842, eyr;

    cout << "give me a number: ";
    cin >> eyr;
    
    cout << "the " << eyr << " in:\n dolar: "<< setprecision(3) << eyrdol*eyr <<"\n yen: "<< setprecision(3) << eyryen*eyr <<"\n elv.fragko: "<< setprecision(3) << eyrelvfrang*eyr <<"\n sterlina: " << setprecision(3) << eyrsterl*eyr <<endl;

    return 0;
}