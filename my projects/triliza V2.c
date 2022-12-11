#include <stdio.h>
#include <time.h>
#include <stdbool.h>
#include <stdlib.h>

int user_sellect_P_1_or_2(); // Here I ask the user for the number 1 or 2
int finished_yet(char table[][]);
void show_triliza(char triliza[][]);
int search_for(char search, char triliza[][]);

int main(void) {
    
    srand(time(0));

    int user, COM, C_user, random_number, score[2] = {0 ,0}, finish 
    
    char triliza[2,2];

    _Bool flag_continue_game = true;

    random_number = rand(); // Here I find a random number based to time so it is always a random number

    C_user = (random_number / 2) + 1; // Here I declere a random Current user to start the game

    user = user_sellect_P_1_or_2();

    if(user == 1){
        COM = 2;
    }else{
        COM = 1;
    }

    while(flag_continue_game){
    
    if(COM == C_user){
        //random cords of COM


        C_user = user;
    }else if(user == C_user){
        //user select cord


        C_user = COM;
    }

    show_triliza(triliza);

    finish = finished_yet(triliza); // Here finish is the player that wins and or the draw (this meens that it checks if the table is full or not)

    if(finish == 1){}

    return 0;
}

int user_sellect_P_1_or_2(){

    int Player_number;

    do{

        printf("Player 1 or 2 ?");
        scanf("%d", &Player_number);
        if(player_number != 1 && player_number != 2){
            printf("Sorry not what i asked for...\nPlease try again.\n");
        }

    }while(Player_number != 1 && Player_number != 2);

    return Player_number;
}

int finished_yet (char triliza[][]){
    int finished;
    char search = 'X';
    
    finished = search_for(search, triliza);
    search = 'O';
    finished = search_for(search, triliza);

    return finished;
}

void show_triliza(char triliza[][]){
    printf("%c | %c | %c \n",triliza[0][0], triliza[0][1], triliza[0][2]);
    printf ("--+----+----\n");
    printf("%c | %c | %c \n",triliza[1][0], triliza[1][1], triliza[1][2]);
    printf ("--+----+----\n");
    printf("%c | %c | %c \n",triliza[2][0], triliza[2][1], triliza[2][2]);
}

int search_for (char search, char triliza [][]){
    //here i search for the X and O and if a player wins
}
