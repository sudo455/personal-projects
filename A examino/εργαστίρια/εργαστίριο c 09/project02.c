#include <stdio.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void){
    int i, j;
    printf("give me two random numbers (x, y): ");
    scanf("%d, %d", &i, &j);
    printf("x=%d, y=%d\n", i, j);
    swap(&i, &j);
    printf("the final result is x=%i y=%i\n", i, j);

    return 0;
}