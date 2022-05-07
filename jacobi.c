#include <stdio.h>

#define ROWS 4

void jacobi(double A[ROWS][ROWS], double B[ROWS], double chute[ROWS], int n){
    double next[ROWS];
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
            next[i] = bi;
        }
        printf("\n");
        //atualizar o chute
        for(int i = 0; i < ROWS; i++){
            chute[i] = next[i];
        }
    }
}

int main(){
    double A[ROWS][ROWS] = {
        {-10.33,-3.04,4.4,0.96},
        {4.11,-8.38,-0.62,-1.72},
        {1.38,2.62,-10.22,-4.28},
        {-1.57,1.17,-3.39,-8.07}};
    double B[ROWS][ROWS] = {-0.86,-1.41,3.41,-1.94};

    double chute[ROWS] = {-1.64,0.41,-3.0,0.32};
    int n = 16;

    jacobi(A,B,chute, n);
}