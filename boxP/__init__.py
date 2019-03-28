import numpy as np


def boxp(input_32=[]):
    output_32 = []
    Pbox = np.array([16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
                     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25])
    for i in range(32):
        output_32.append(input_32[Pbox[i] - 1])

    return output_32
