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
    // −2/9⋅L2→L2 
   for(int i = 0; i < COL; i++){
        matriz[1][i] *= (-2.0/9.0);
    }
    // −1/3⋅L4+L3→L3
    for(int i = 0; i < COL; i++){
        matriz[2][i] = ((-1.0/3.0)*matriz[3][i]) + matriz[2][i];
    }
    // −5/6⋅L3→L3 
    for(int i = 0; i < COL; i++){
        matriz[2][i] *= (-5.0/6.0);
    }
    //L2↔L3  
    for(int k=0;k<COL;k++){
        double temp = matriz[1][k];
        matriz[1][k] = matriz[2][k];
        matriz[2][k] = temp;
    }
    //L1↔L4  
    for(int k=0;k<COL;k++){
        double temp = matriz[0][k];
        matriz[0][k] = matriz[3][k];
        matriz[3][k] = temp;
    }
    // 5⋅L3+L2→L2
    for(int i = 0; i < COL; i++){
        matriz[1][i] = ((-5.0/1.0)*matriz[2][i]) + matriz[1][i];
    }

    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
        {1.0/6.0, -9.0/4.0,-4.0/3.0},
        {-1.0/6.0,1.0/2.0,2.0/1.0},
        {-1.0/9.0,-1.0/9.0,8.0/7.0},
        {-4.0/1.0,4.0/5.0,-4.0/3.0}
    };
    printf("matriz[0][0]: %.16f \n", matriz[0][0]);

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}