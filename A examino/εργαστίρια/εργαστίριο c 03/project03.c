#include <stdio.h>

int main(){
    int i,j,k;
    printf("loop|n!\n");
    for(i = 1; i <=10; i++) {
       k=1;
       for(j =1; j<=i; j++) {
           k=k*j;
       }
       printf("%d|%d\n", i, k);
    }
    return 0;
}