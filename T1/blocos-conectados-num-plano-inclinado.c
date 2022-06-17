#include <stdio.h>
#include <math.h>
#define L 3
#define C 3

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            chute[i]=bi;
        }
        printf("\n");
    }
}


int main() {
    double g = 9.81, k = 54 * M_PI/180,
            u1 = 0.2, u2 = 0.26, u3 = 0.52,
            m1 = 186, m2 = 168, m3 = 35,
            a = (m1 * g * sin(k)) - (u1 * m1 * g * cos(k)),
            T = (m2 * g * sin(k)) - (u2 * m2 * g * cos(k)),
            R = (m3 * g * sin(k)) - (u3 * m3 * g * cos(k));

    printf("%.16f,   %.16f,   %.16f", a, T, R);

    // Seidel input
    double A[L][C] = {{m1, 1, 0},
                            {m2, -1, 1},
                            {m3, 0, -1}
    };

    double B[L] = {a, T, R};

    double chute[C] = {5, 148, 127};

    int n = 300;

    jacobi(A,B,chute,n);

    return 0;
}
