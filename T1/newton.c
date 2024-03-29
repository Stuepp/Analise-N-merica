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
        double B = 16.47, H = 8.81;
        return B*(H - (4*x)) + (4*x)*((3*x) - H);
    }
    double df(double x){
         double B = 16.47, H = 8.81;
        return -4*(B+H - 6*x);
    }

    double x0=2.16;
    int n = 5;

    newton(f, df, x0,n);
}