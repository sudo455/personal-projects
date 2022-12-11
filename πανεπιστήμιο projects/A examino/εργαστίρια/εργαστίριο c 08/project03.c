 #include <stdio.h>

int s_count(char string[], char character);

int main(void){
    char string[50], character;
    int result;
    printf("give me a string: ");
    scanf("%49s", string);
    printf("give me a character: ");
    scanf(" %c", &character);
    result = s_count(string, character);
    printf("the result is %d\n", result);
    return 0;
}

int s_count(char string[], char character){
    int i, count = 0;
    for(i = 0;string[i]!='\0';i++){
        if(string[i]==character){
            count++;
        }
    }
    return count;
}