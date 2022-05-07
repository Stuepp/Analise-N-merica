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
            printf(" x %d^(%d) = %.16f", i+1, k+1, bi);
            chute[i] = bi;
        }
        printf("\n");
    }
}

int main(){
    double A[ROWS][ROWS] = {{-4.22,1.66,-0.96},{-2.24,4.62,0.78},{-3.52,-2.36,-7.48}};
    double B[ROWS][ROWS] = {2.03,2.36,4.92};

    double chute[ROWS] = {-3.63,1.88,-2.23};
    int n = 18;

    jacobi(A,B,chute, n);
}