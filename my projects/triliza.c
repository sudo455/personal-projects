#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

void show_table_triliza(int table[2][2],int cords_X,int cords_Y, int player_current, char table2[2][2], bool flag_start_game){ //this will show the table of triliza   
    if(player_current == 1 && flag_start_game == false){
        table2[cords_X][cords_Y] = 'X';
    }else if(player_current == 2 && flag_start_game == false){
        table2[cords_X][cords_Y] = 'O';
    }else{
        for(int i = 0; i <= 2; i++){
            for(int j = 0; j<= i; j++){
                table2[i][j] ='N';
            }
        }
    }
    printf("table2:\n\n");
    printf("   x \n y   1   2   3 \n   1 %c | %c | %c \n    ---+---+---\n   2 %c | %c | %c\n    ---+---+---\n   3 %c | %c | %c\n\n", table2[0][0], table2[0][1], table2[0][2], table2[1][0], table2[1][1], table2[1][2], table2[2][0], table2[2][1], table2[2][2]);
    printf("table:\n\n");
    printf("   x \n y   1   2   3 \n   1 %i | %i | %i \n    ---+---+---\n   2 %i | %i | %i\n    ---+---+---\n   3 %i | %i | %i\n\n", table[0][0], table[0][1], table[0][2], table[1][0], table[1][1], table[1][2], table[2][0], table[2][1], table[2][2]);
}

int random_sellect_cords(int long long random_number, int table[2][2]){
    bool flag_continue = false;
    int random_cords;

    while(!flag_continue){
        random_cords = (rand()*random_number)%3;
        if(random_cords<0){
            random_cords = random_cords*(-1);
        }
        if(random_cords >= 1 && random_cords <= 3){
            flag_continue = true;
        }
        else{
            random_number = (rand()%3)*2+random_number+2;
        }
    }
    return random_cords;
}

int user_sellect_cords(int player, char cord){
    int x;
    do{
        printf("player %i give me the %c cords:", player, cord);
        scanf("%i",&x);
        printf("\n");
        if (x>3 || x<1){
            printf("Sorry wrong number \n try again\n");
        }
    } while (x>3 || x<1);
    return x;
}

int main(void) {
    // random number is the seed of the random number generator
    // random random sell X and Y is the COM(comuter) that desides the next move in the game
    int player_random,player_COM, win, x, y, table_triliza[2][2], player_user, player_current, random_sell_X, random_sell_Y, repeat_break_user, repeat_break_COM,i,j;
    int long long random_number;
    bool flag_continue, flag_start_game;
    char cord, table_triliza_2[2][2];
    
    repeat_break_user=0;
    repeat_break_COM=0;
    player_current=0;
    win=0;
    x=0;
    y=0;
    flag_start_game=true;
    
    //this will 0 out the table of triliza
    for(i = 0; i<= 2;i++){ 
        for(j = 0; j <= 2;j++){
            table_triliza[i][j] = 0;
        }
    }
    printf("%d %d %d \n",table_triliza[0][0], table_triliza[0][1], table_triliza[0][2]);
    printf("%d %d %d \n",table_triliza[1][0], table_triliza[1][1], table_triliza[1][2]);
    printf("%d %d %d \n",table_triliza[2][0], table_triliza[2][1], table_triliza[2][2]);


    printf("Disclaymer N in the table is null (nothing in the cell)\n.\n.\n");

    // here the user gives a random number
    printf("give me a random number:");
    scanf("%lld", &random_number);
    printf("\n");
    flag_continue = false;
    while(!flag_continue){
        player_random = rand()*random_number%2+1;
        if(player_random < 0 ){
            random_number++;
        }
        else {
            flag_continue = true;
        }
    }
    player_current = player_random;
    
    // here the user will select the player 1 or 2 only
    do 
    {
        printf("Player 1 or 2(1 is X and 2 is O): ");
        scanf("%d", &player_user);
        printf("\n");
        if (player_user != 1 && player_user != 2) {
            printf("Sorry wrong number try again\n");
        }
    } while (player_user != 1 && player_user != 2);
    
    // here the COM will select wether is player 1 or player 2
    if(player_user == 2){
        player_COM = 1;
    }else if(player_user == 1){
        player_COM = 2;
    }

    // here announce which player will sart
    printf("player %i will now begin \n\n", player_random);
    show_table_triliza(table_triliza, x ,y ,player_current, table_triliza_2, flag_start_game);
    flag_continue= false;

    //actuall game:
    while(win == 1 && (repeat_break_user <= 2 && repeat_break_COM <= 2)){
        if(player_current == player_user){
            
            flag_continue = false;
            cord='X';
            while(!flag_continue){
                x=user_sellect_cords(player_current, cord);
                //here we check if the player can put the simbol to the table
                if(table_triliza[x-1][0] == 0 || table_triliza[x-1][1] == 0 || table_triliza[x-1][2] == 0){
                    flag_continue = true;
                } else {
                    printf("Sorry array full\n");
                }
            }

            flag_continue = false;
            cord='Y';
            while(!flag_continue){
                y=user_sellect_cords(player_current, cord);
                if(table_triliza[x-1][y-1] == 0){
                    flag_continue = true;
                }else {
                    printf("Sorry column full\n");
                }
            }

            repeat_break_user+=1;
            repeat_break_COM=0;

            table_triliza[x-1][y-1]=player_current;
            show_table_triliza(table_triliza, x-1, y-1, player_current, table_triliza_2, flag_start_game);

            player_current=player_COM;
        }
        else if (player_current == player_COM){
            flag_continue = false;
            while(!flag_continue){
                random_sell_X=random_sellect_cords(random_number, table_triliza);
                if(table_triliza[random_sell_X][0] == 0 || table_triliza[random_sell_X][1] == 0 || table_triliza[random_sell_X][2] == 0){
                    flag_continue = true;
                }
            }
            while(!flag_continue){
                random_sell_Y=random_sellect_cords(random_number, table_triliza);
                if(table_triliza[random_sell_X][random_sell_Y] == 0 || table_triliza[random_sell_X][random_sell_Y] == 0 || table_triliza[random_sell_X][random_sell_Y] == 0){
                    flag_continue = false;
                }
            }
            printf("player %i(COM) plays X=%i and Y=%i\n", player_current, random_sell_X+1, random_sell_Y+1);

            repeat_break_COM+=1;
            repeat_break_user=0;

            table_triliza[random_sell_X][random_sell_Y]=player_current;
            show_table_triliza(table_triliza, random_sell_X, random_sell_Y, player_current, table_triliza_2, flag_start_game);

            player_current = player_user;
        }
        else{
            printf("Something went wrong\n");
            break;
        }
        // here is the resault tht will be used for the end of the programm
        for(i=0; i<= 2; i++){
            
        }
    }
    if (repeat_break_COM == 3 || repeat_break_user == 3){
        if (repeat_break_user > 0) {
            printf("triliza ended because of breaking value of repeat_break_user \n");
        }else if (repeat_break_COM > 0) {
            printf("triliza ended because of breaking value of repeat_break_COM \n");
        }
    }
    return 0;
}
