#include <stdio.h>

int main(){
    int a, b ,c;
    printf("give me the 1st side of a triangle:");
    scanf("%d", &a);
    printf("give me the 2st side of a triangle:");
    scanf("%d", &b);
    printf("give me the 3st side of a triangle:");
    scanf("%d", &c);
    if((a + b > c) && (b+c > a) && (c + a > b)){
        printf("to trigono einai:\n");
        if(a == b && b == c){
            printf("isopleyro \n");
        }else if (a == b || a == c ||  b == c){
            printf("isoskeles \n");
        }else{
            printf("skalino \n");
        }
    }else{
        printf("den einai trigono \n");
    }
    return 0;
}