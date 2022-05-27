main()

function bissection(f, a, b, n){
    if(f(a) * f(b) >= 0){
        print('Não é possível usar Bolzano para garantir a existência de uma raiz em [%4.f,%4.f]', a, b)
    }
}
function main(){
    function f(x){
        let b = 16.47, h = 8.81
        return b*(h - (4*x)) + (4*x)*((3*x) - h);
    }
    let a = 0
    let b = 0
    let n = 12

    function P(x){
        let porc = 0.25
        let n = 117417491, infec = n*porc,
            lamb = 1.41*pow(10,-10), exp = lamb*(n+1)*x;
        return ((n+1.0) / (1.0 + (n*pow(Math.exp(1),-exp)))) - infec;
    }
    let a1 = 0
    let b1 = 2245
    let n1 = 12

    //bissection(f, a, b, n)
    bissection(P, a1, b1, n1)
}