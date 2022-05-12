#include <stdio.h>

int main(){
    /*
    double R = 129.6429154508417700 / 1.3313859635636867,
        T = (94.6204650062613270 + R) / 1.8100737442604702,
        a = (585.5643000000001200 - T) / 71.8700000000000050;
    printf("R: %.16f \n", R);
    printf("T: %.16f \n", T);
    printf("a: %.16f \n", a);
    */
    /*
    double x3 = 203.0600127086995600 / 1.3164556962025316,
        x2 = (257.1778961324035900 + (x3)) / 1.7752808988764044,
        x1 = (405.5658495930353000 + (x2)) / 178.0000000000000000;
    printf("x1: %.16f \n", x1);
    printf("x2: %.16f \n", x2);
    printf("x3: %.16f \n", x3);*/
    double areia = 4980.0, cascalhoFino = 5488.0, cascalhoGrosso = 3333.0;
    double mina1 = 0.47*areia + 0.34*cascalhoFino + 0.19*cascalhoGrosso;
    double mina2 = 0.31*areia + 0.57*cascalhoFino + 0.12*cascalhoGrosso;
    double mina2 = 0.31*areia + 0.57*cascalhoFino + 0.12*cascalhoGrosso;
    return 0;
}