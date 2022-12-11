#include <stdio.h>

void substring(char source[], int start, int count, char result[]);

int main(void){
    char source[40], result[40];
    int start, count;
    printf("give me a string: ");
    scanf("%s", source);
    printf("give me the start and the count (start, count): ");
    scanf("%d, %d", &start, &count);
    substring(source, start, count, result);
    printf("the result is:\n %s\n", result);
    return 0;
}

void substring(char source[], int start, int count, char result[]){
    int i, j=0;
    for(i = start; i < count && source[i] != '\0'; i++){
        result[j] = source[start + i];
        j++;
    }
    result[i] = '\0';
}