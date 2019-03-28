import numpy as np


# 输入为32位列表，输出为48位列表
def boxe(input_32=[]):
    output_48 = []
    Ebox = np.array([[32, 1, 2, 3, 4, 5],
                     [4, 5, 6, 7, 8, 9],
                     [8, 9, 10, 11, 12, 13],
                     [12, 13, 14, 15, 16, 17],
                     [16, 17, 18, 19, 20, 21],
                     [20, 21, 22, 23, 24, 25],
                     [24, 25, 26, 27, 28, 29],
                     [28, 29, 30, 31, 32, 1],
                     ])

    for i in range(8):
        for j in range(6):
            output_48.append(input_32[Ebox[i][j] - 1])
    return output_48
