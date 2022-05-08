#include <stdio.h>
#include <math.h>

#define ROW 4
#define COL 3

void imprimeMatriz(double matriz[ROW][COL]){
    for(int row = 0; row < ROW; row++){
        for(int col = 0; col < COL; col++){
            printf("%.16f ", matriz[row][col]);
        }
        printf("\n");
    }
}

void operacoes(double matriz[ROW][COL]){
    // −8/3⋅L3+L4→L4
    for(int i = 0; i < COL; i++){
        matriz[3][i] = ((-8.0/3.0)*matriz[2][i]) + matriz[3][i];
    }
    // −7/3⋅L3+L1→L1
    for(int i = 0; i < COL; i++){
        matriz[0][i] = ((-7.0/3.0)*matriz[2][i]) + matriz[0][i];
    }
    // 5/3⋅L2→L2
   for(int i = 0; i < COL; i++){
        matriz[1][i] *= (5.0/3.0);
    }
    // −1/2⋅L4→L4 
    for(int i = 0; i < COL; i++){
        matriz[3][i] *= (-1.0/2.0);
    }
    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
        {9.0/2.0, 4.0/7.0,-3.0/4.0},
        {-9.0/5.0,1.0/7.0,8.0/7.0},
        {-4.0/9.0,4.0,-1.0},
        {1.0/2.0,-8.0/9.0,9.0/4.0}
    };
    printf("matriz[0][0]: %.16f \n", matriz[0][0]);

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}