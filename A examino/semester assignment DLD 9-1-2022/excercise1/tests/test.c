// Πρόγραμμα εμφάνισης χαρακτήρων μέχρι το τέλος του αρχείου
#include <stdio.h>

int main (void){
	int c;
    FILE *in;

    in = fopen("test_text.txt", "r");
	
	while ( !feof(in) ){
        c = 
		putchar (c);
		printf ("pass \n");
	}
	return 0;
    fclose(in);
}

/* gcc test.c -o test  */