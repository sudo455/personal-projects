#include <stdio.h>

double solve (double n){
    double x = 0;
    if(n!=0){
        x=solve(n-1) + 1/n;
        return x;
    }
}

int main(void){
    int user_number;
    double parastash;
    do{
        printf("give me a numbrt between 1 and 100:");
        scanf("%d",&user_number);
        if(user_number < 1 || user_number > 100){
            printf("whrong number try again.\n");
        }
    }while(user_number < 1 || user_number > 100);

    parastash = solve(user_number);

    printf("parastash =%.3f\n", parastash);
    return 0;
}