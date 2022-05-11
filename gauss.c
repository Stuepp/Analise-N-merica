#include <stdio.h>

#define ROWS 3
#define COLS 4

void print_matrix(double matrix[ROWS][COLS]){
    for(int i=0; i < ROWS; i++){
        for(int j = 0; j < COLS; j++){
            printf("%.16f\t", matrix[i][j]);
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
    double m1 = 68.68, m2 = 56.25, m3 = 44.49,  // massas
     c1 = 9.99, c2 = 15.51, c3 = 20.94, // coefs de arrasto
     v = 9.95, // velocidade
     g = 9.81; // gravidade
    double E[ROWS][COLS] = {
        {m1,1.0,0.0,(m1*g)-(c1*v)},
        {m2,-1.0,1.0,(m2*g)-(c2*v)},
        {m3,0.0,-1.0,(m3*g)-(c3*v)}
    };

    print_matrix(E);
    printf("\n");
    gauss(E);

    //reverse_sub(E);
}