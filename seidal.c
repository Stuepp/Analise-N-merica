#include <stdio.h>
//corrigir!!!
#define ROWS 3

void jacobi(double A[ROWS][ROWS], double B[ROWS], double chute[ROWS], int n){
    for(int k = 0; k < n; k++){
        for(int i = 0; i < ROWS; i++){
            double bi = B[i];
            for(int j = 0; j< ROWS; j++){
                if(j != i){
                    bi -= A[i][j] * chute[j];
                }
            }
            bi /= A[i][i];
            printf("x %d^(%d) = %.16f", i+1, k+1, bi);
            chute[i] = bi;
        }
        printf("\n");
    }
}

int main(){
    double A[ROWS][ROWS] = {{4,1,-1},{-1,3,1},{1,-1,5}};
    double B[ROWS][ROWS] = {5,6,4};

    double chute[ROWS] = {-1-1,-1};
    int n = 5;

    jacobi(A,B,chute, n);
}