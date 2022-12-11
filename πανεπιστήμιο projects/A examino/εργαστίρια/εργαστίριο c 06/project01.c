#include <stdio.h>

void show(int number) {
    printf("number=%d\n", number*number*number);
}

int main(void) {
    int number;
    do {
        printf("give me a number[0-100]");
        scanf("%d",&number);
        printf("\n");
        if(number > 100 || number < 0 ) {
            printf("Sorry wrong number try again\n");
        }
    }while (number>=100 || number<=0 );
    show(number);
    return 0;
}