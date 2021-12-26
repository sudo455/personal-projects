#include <stdio.h>

struct IP { // IP = individual person
    char name[20];
    int telephone;
};

struct IP input_person(){
    struct IP input_person;
    printf("name : telephone\n");
    scanf("%19s : %d", input_person.name, &input_person.telephone);
    return input_person;
}

int main(void){
    int i;
    struct IP NAT[4]; //NAT = Name And Telephone
    printf("give me:\n");
    for(i = 0; i < 5 ; i++) {
        NAT[i] = input_person();
    }
    printf("Names : telephone\n");
    for(i = 0; i <5; i++){
        printf("%20s : %d\n", NAT[i].name, NAT[i].telephone);
    }
    return 0;
}