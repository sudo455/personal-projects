#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

class Student{
    private:
        static int count;
        string name;
        int am;
    public:
        Student(string nme){
            count ++;
            am = count;
            name=nme;
            print_s(name, am);
        }

        void print_s(string nme, int am){

            cout << "Αριθμός Μητρώου: " << setfill('0') << setw(3) << am << "Όνομα: " << nme << endl;

        }

};
int Student::count = 0;

int main() {
    Student student1("Αλίκη Παλαιολόγου");
    Student student2("Άγγελος Μωραΐτης");
    Student student3("Άκης Πεπόνης");

    return 0;
}