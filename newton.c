#include <stdio.h>
#include <math.h>

void newton(double (*f)(double), double (*df)(double), double x0, int n){
    double der = df(x0);
    if(df(x0) == 0){
        printf("solha outra estimativa inicial.");
    } else{
        for(int i = 0; i<n;i++){
            double x1 = x0 -f(x0) / der;
            der = df(x1);
            if(der == 0){
                printf("x_%d = %.16f (precisei parar)\n", i+1,x1);
                return;
            } else {
                printf("x_%d  %.16f\n",i+1,x1);
            }
            x0 = x1;
        }
    }
}

int main(){
    double f(double x){
        return pow(M_E,(5*x)) -2;
    }
    double df(double x){
        return 2*x - 4 -1/x;
    }

    double x0=-1.16164621;
    int n = 700;

    newton(f, df, x0,n);
}