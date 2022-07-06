#include <stdio.h>

int main(void){
    int x = 455;;
    double y = 666.156455;
    const char character = 'Μ';
    char *string = "Άγγελος Μωρ";

    printf("the value of %i is located in %p \n", x, &x);
    printf("the value of %lf is located in %p \n", y, &y);
    printf("the value of %c is located in %p \n", character, &character);
    printf("the value of %s is located in %p \n", string, &string);
    return 0;
}