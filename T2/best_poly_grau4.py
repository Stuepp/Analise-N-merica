import numpy as np
# import scipy as sp

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)

x = [-4.4897, -4.3589, -4.2792, -4.1985, -4.0981, -3.9363, -3.8258, -3.7316, -3.684, -3.5581, -3.4651, -3.4183, -3.3014, -3.1433, -3.1075, -2.9703, -2.8778, -2.7672, -2.7407, -2.5916, -2.4803, -2.4458, -2.3426, -2.1862, -2.0992, -2.0119, -1.893, -1.8608, -1.7073, -1.5989, -1.5835, -1.4894, -1.3259, -1.2954, -1.1329, -1.0832, -0.9866, -0.8308, -0.7929, -0.6724, -0.5969, -0.5182, -0.3767, -0.3202, -0.2043, -0.0852, 0.0019, 0.0922, 0.1788, 0.345, 0.3676, 0.4792, 0.5628, 0.7046, 0.7354, 0.8681, 0.9434, 1.1011, 1.2144, 1.3089, 1.3655, 1.4285, 1.5916, 1.6285, 1.7546, 1.8468, 1.9676, 2.0504, 2.1094, 2.2258, 2.3284, 2.3944, 2.483, 2.6517, 2.7704, 2.8296, 2.8757, 3.0571, 3.1358, 3.1611, 3.292, 3.407, 3.4898, 3.5972, 3.7028, 3.8361, 3.9303, 3.9781, 4.036, 4.1795, 4.2624, 4.4054, 4.4745, 4.5877, 4.6297, 4.7328, 4.8485, 4.9923]
y = [0.5077, 1.9628, 2.5177, 2.1978, 4.2346, 5.498, 5.0711, 6.4309, 6.9925, 7.065, 7.5741, 6.8735, 6.894, 7.8335, 7.564, 8.0228, 7.3425, 8.8248, 8.0417, 8.0613, 7.6677, 6.8312, 9.2107, 7.2332, 7.7259, 6.8825, 8.6108, 6.9482, 6.2247, 6.1322, 6.1543, 6.1168, 5.4437, 4.6985, 5.0899, 5.2536, 5.1666, 3.5822, 3.8506, 5.0112, 4.4469, 4.5514, 3.5224, 4.3896, 4.0117, 3.0726, 4.1045, 3.9761, 4.5001, 4.2207, 3.98, 4.2102, 4.3632, 4.3124, 4.5389, 4.9027, 4.3314, 5.4364, 5.4076, 6.1855, 5.5947, 5.7408, 6.724, 6.4843, 6.6846, 7.3205, 6.7147, 7.7249, 8.1994, 8.3846, 8.4876, 9.0419, 9.1013, 10.384, 9.6363, 9.0903, 10.091, 10.3441, 10.9519, 10.5762, 10.1949, 11.7985, 11.2883, 12.6051, 10.7027, 11.0623, 10.8438, 10.9078, 9.612, 10.3006, 10.2689, 9.2572, 9.036, 8.6177, 8.4614, 8.7898, 6.5356, 4.909]

a0, a1, a2, a3, a4 = best_poly(x, y, 4)

print(f'{a0 = } , {a1 = }, {a2 = }, {a3 = }, {a4 = }')