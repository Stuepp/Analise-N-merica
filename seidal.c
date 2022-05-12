#include <stdio.h>
#include<math.h>
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
    /*double A[ROWS][ROWS] = {
        {10.68,2.24,-2.13,-4.6},
        {0.7,-6.66,0.27,3.98},
        {-0.21,2.65,-5.76,1.19},
        {3.81,-2.26,-3.85,11.64}
    };
    double B[ROWS][ROWS] = {-3.63,-3.99,-3.84,4.36};

    double chute[ROWS] = {3.44,-2.32,3.35,-4.49};
    int n = 16;

    jacobi(A,B,chute, n);*/
    double m1 = 178, m2 = 138, m3 = 100,  // massas
        u1 = 0.25, u2 = 0.44, u3 = 0.54, // const. da mola
        g = 9.81, // gravidade
        alpha = 44, // angulo
        a = (m1 * g * sin(alpha)) - (u1 * m1 * g * cos(alpha)),
        T = (m2 * g * sin(alpha)) - (u2 * m2 * g * cos(alpha)),
        R = (m3 * g * sin(alpha)) - (u3 * m3 * g * cos(alpha));

        printf("a = %.16f\n",a);
        printf("T = %.16f\n",T);
        printf("R = %.16f\n",R);

        // Seidal Input
        double A[3][3] = {
            {m1, 1.0, 0.0},
            {m2, -1.0, 1.0},
            {m3, 0.0, -1.0}
        };
        double B[3] = {a,T,R};
        double chute[3] = {5, 148, 127};
        int n = 300;

        jacobi(A,B,chute,n);
}