#include <stdio.h>

int main(void){
    int i, user_number;
    do{
        printf("give me a numbrt between 1 and 20:");
        scanf("%d",&user_number);
        if(user_number < 1 || user_number > 20){
            printf("whrong number try again.\n");
        }
    }while(user_number < 1 || user_number > 20);
    printf("start  |  start*3\n-----------------\n");
    for(i = 1; i <= user_number; i++){
        printf("  %d    |     %d   \n", i, i*3);
    }
    return 0;
}