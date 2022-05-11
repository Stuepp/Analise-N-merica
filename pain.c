#include <stdio.h>
#include <math.h>

#define ROW 4
#define COL 4

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

void operacaoEmLinha(double matriz[ROW][COL], int row, double num){
    for(int i = 0; i < COL; i++){
        matriz[row][i] *= num; 
    }
}

void opercaoEmDuasLinhas(double matriz[ROW][COL], int target, int r2, double num){
    for(int i = 0; i < COL; i++){
        matriz[target][i] = (num*matriz[r2][i]) + matriz[target][i];
    }
}

void operacoes(double matriz[ROW][COL]){
    // −7/5⋅L1+L2→L2
    opercaoEmDuasLinhas(matriz, 1, 0, (-7.0/5.0));
    // −2/5⋅L1+L3→L3 
    opercaoEmDuasLinhas(matriz, 2, 0, (-2.0/5.0));
    // −4/5⋅L1+L4→L4 
    opercaoEmDuasLinhas(matriz, 3, 0, (-4.0/5.0));
    // 17/18⋅L2+L3→L3
    opercaoEmDuasLinhas(matriz, 2, 1, (17.0/18.0));
    // −41/18⋅L2+L4→L4
    opercaoEmDuasLinhas(matriz, 3, 1, (-41.0/18.0));
    // 53/38⋅L3+L4→L4
    opercaoEmDuasLinhas(matriz, 3, 2, (53.0/38.0));

    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
        {-5.0/1.0, 4.0/1.0,-4.0/1.0, 3.0/1.0},
        {-7.0/1.0,2.0/1.0,4.0/1.0,-6.0/1.0},
        {-2.0/1.0,5.0/1.0,2.0/1.0,-1.0/1.0},
        {-4.0/1.0,-5.0/1.0,1.0/1.0,-2.0/1.0}
    };

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}