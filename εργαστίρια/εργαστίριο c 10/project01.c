/*this is a lab 9 excercise so yea*/
#include <stdio.h>

struct element{
    struct element *prev;
    int value;
    struct element *next;
};

void print_element_next(struct element *);
void print_element_prev(struct element *);

int main(void) {
    struct element n1, n2, n3, n4, n5;
    struct element *list_ptr = &n1;
    
    n1.prev = (struct element *) 0;
    n1.value = 0;
    n1.next = &n2;

    n2.prev = &n1;
    n2.value = 0;
    n2.next = &n3;

    n3.prev = &n2;
    n3.value = 0;
    n3.next = &n4;
    
    n4.prev = &n3;
    n4.value = 0;
    n4.next = &n5;
    
    n5.prev = &n4;
    n5.value = 0;
    n5.next = (struct element *) 0;
    
    while ( list_ptr != (struct element *) 0 ) {
		printf ("give me a random number: ");
        scanf ("%i", &list_ptr->value);
		list_ptr = list_ptr->next;
	}
    list_ptr = &n1;
    print_element_next(list_ptr);
    printf ("\n");
    list_ptr = &n5;
    print_element_prev(list_ptr);

    return 0;
}

void print_element_next (struct element *prnt_e) {
    while ( prnt_e != (struct element *) 0 ) {
		printf ("%i\n", prnt_e->value);
		prnt_e = prnt_e->next;
	}
}

void print_element_prev (struct element *prnt_e) {
    while ( prnt_e != (struct element *) 0 ) {
		printf ("%i\n", prnt_e->value);
		prnt_e = prnt_e->prev;
	}
}