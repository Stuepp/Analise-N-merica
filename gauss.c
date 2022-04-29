#include <stdio.h>

#define ROWS 4
#define COLS 5

void print_matrix(double matrix[ROWS][COLS]){
    for(int i=0; i < ROWS; i++){
        for(int j = 0; j < COLS; j++){
            printf("%f\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void gauss(double E[ROWS][COLS]){
    for(int j =0; j< COLS -2; j++){
        for(int i=j; i<ROWS;i++){
            if(E[i][j] != 0){
                if(i!=j){
                    //é preciso trocar linhas
                    for(int k=0;k<COLS;k++){
                        double temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }
                }
                //aplicar operações elementares em linha
                // a * Lj + Lm -> Lm
                for (int m = j+1; m<ROWS;m++){
                    double a = -E[m][j]/E[j][j];
                    for(int n=j;n<COLS;n++){
                        E[m][n] += a * E[j][n];
                    }
                }
                print_matrix(E);
                printf("\n");
                break;
            }
        }
    }
}

void reverse_sub(double E[ROWS][COLS]){
    int last = ROWS - 1;
}

int main(){
    double E[ROWS][COLS] = {
        {2,4,6,2,4},
        {1,2,-1,3,8},
        {-3,1,-2,1,-1},
        {1,3,-3,-2,6}
    };

    print_matrix(E);
    printf("\n");
    gauss(E);

    //reverse_sub(E);
}