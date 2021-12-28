#include <stdio.h>

void print_addr(int x);
void print_addr_ptr(int *x);
int main (void) {
    int x;
    printf("give me a random number: ");
    scanf("%d", &x);
    print_addr(x);
    print_addr_ptr(&x);
    return 0;
}

void print_addr(int x) {
    printf("\nThe value of %d in the function print_addr is stored in the address: %p\n", x, &x);
}

void print_addr_ptr(int *x) {
    printf("\nThe value of %d in the function print_addr_ptr is stored in the address: %p\n", *x, x);
}