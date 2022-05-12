#include <stdio.h>
#include <math.h>

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
    /*double m1 = 178, m2 = 138, m3 = 100,  // massas
     u1 = 0.25, u2 = 0.44, u3 = 0.54, // const. da mola
     g = 9.81, // gravidade
     alpha = 44; // angulo
    double E[ROWS][COLS] = {
        {m1, 1.0, 0.0, (m1 * g * sin(alpha)) - (u1 * m1 * g * cos(alpha))},
        {m2, -1.0, 1.0 , (m2 * g * sin(alpha)) - (u2 * m2 * g * cos(alpha))},
        {m3, 0.0, -1.0, (m3 * g * sin(alpha)) - (u3 * m3 * g * cos(alpha))}
    };*/
    double v = 9.99,
        m1 = 71.87, m2 = 58.22, m3 = 43.11,
        c1 = 11.96, c2 = 19.16, c3 = 23.29,
        g = 9.81;

    double E[ROWS][COLS] = {
        {m1, 1.0, 0.0, (m1*g) - (c1*v)},
        {m2, -1.0, 1.0, (m2*g) - (c2*v)},
        {m3, 0.0, -1.0, (m3*g) - (c3*v)}
    };

    print_matrix(E);
    printf("\n");
    gauss(E);

    //reverse_sub(E);
}