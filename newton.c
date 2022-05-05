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
        double r = 4.73, ps = 134.03, pw = 1000,
            Vesfera = (4.0/3.0) * M_PI * pow(r,3),
            V = Vesfera - ((ps * Vesfera) / pw);
        return (((M_PI * pow(x,2)) / 3.0) * ((3*r) - x)) - V;
    }
    double df(double x){
        double r = 4.73;
        return x*((6.28319*r) - (3.14159*x));
    }

    double x0=3.7;
    int n = 5;

    newton(f, df, x0,n);
}