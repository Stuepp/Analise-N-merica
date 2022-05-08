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

void trocaLinha(double matriz[ROW][COL], int r1, int r2){
        for(int k=0;k<COL;k++){
        double temp = matriz[r1][k];
        matriz[r1][k] = matriz[r2][k];
        matriz[r2][k] = temp;
    }
}

void operacoes(double matriz[ROW][COL]){
    // 1/3⋅L3+L2→L2
    for(int i = 0; i < COL; i++){
        matriz[1][i] = ((1.0/3.0)*matriz[2][i]) + matriz[1][i];
    }
    //L2↔L4
    trocaLinha(matriz, 1, 3);
    // 7/8⋅L1→L1
   for(int i = 0; i < COL; i++){
        matriz[0][i] *= (7.0/8.0);
    }
    //L2↔L3  
    trocaLinha(matriz,1,2);
    // −7/5⋅L4→L4
    for(int i = 0; i < COL; i++){
        matriz[3][i] *= (-7.0/5.0);
    }
    // 1/3⋅L2+L3→L3
    for(int i = 0; i < COL; i++){
        matriz[2][i] = ((1.0/3.0)*matriz[1][i]) + matriz[2][i];
    }

    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
        {1.0/1.0, -4.0/3.0,2.0/3.0},
        {-7.0/9.0,-7.0/4.0,-1.0/2.0},
        {-1.0/6.0,7.0/3.0,4.0/5.0},
        {8.0/3.0,9.0/4.0,-2.0/3.0}
    };
    printf("matriz[0][0]: %.16f \n", matriz[0][0]);

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}