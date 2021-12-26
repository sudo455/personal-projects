#include <stdio.h>
#include <string.h>

struct person{
    char name[20];
    int age;

};

int main(void){
    struct person person1, person2;
    //person1.name = "something";
    //does not work like that for that reason i'll use the strcpy() function (???)
    strcpy(person1.name,"something");
    person1.age = 18;
    person2.age = 19;
    strcpy(person2.name,"somethingwith25chardssae");


    printf("%s : %d\n %s : %d\n", person1.name, person1.age, person2.name, person2.age);


    return 0;
}