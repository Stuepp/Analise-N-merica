#include <stdio.h>
//corrigir!!! está ok!
#define ROWS 4

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
    double A[ROWS][ROWS] = {
        {10.68,2.24,-2.13,-4.6},
        {0.7,-6.66,0.27,3.98},
        {-0.21,2.65,-5.76,1.19},
        {3.81,-2.26,-3.85,11.64}
    };
    double B[ROWS][ROWS] = {-3.63,-3.99,-3.84,4.36};

    double chute[ROWS] = {3.44,-2.32,3.35,-4.49};
    int n = 16;

    jacobi(A,B,chute, n);
}