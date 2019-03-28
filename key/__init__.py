class KEY:
    k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16 = [], [], [], [], [], [], [], [], [], [], \
                                                                            [], [], [], [], [], []
    pc_1 = list([57, 49, 41, 33, 25, 17, 9, 1,
                 58, 50, 42, 34, 26, 18, 10, 2,
                 59, 51, 43, 35, 27, 19, 11, 3,
                 60, 52, 44, 36, 63, 55, 47, 39,
                 31, 23, 15, 7, 62, 54, 46, 38,
                 30, 22, 14, 6, 61, 53, 45, 37,
                 29, 21, 13, 5, 28, 20, 12, 4])
    pc_2 = list([14, 17, 11, 24, 1, 5,
                 3, 28, 15, 6, 21, 10,
                 23, 19, 12, 4, 26, 8,
                 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55,
                 30, 40, 51, 45, 33, 48,
                 44, 49, 39, 56, 34, 53,
                 46, 42, 50, 36, 29, 32])
    move = list([1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1])

    def key(self, key_64=[]):  # 64位密钥
        input_56 = []
        '''
        key_64 = list([0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1,
                       1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1])
        '''
        for i in range(56):
            input_56.append(key_64[self.pc_1[i] - 1])

        c0 = input_56[0:28]
        d0 = input_56[28:56]
        cn = c0
        dn = d0

        for i in range(16):  # 16轮
            # 左移move[i]个位置
            # 56位
            # kn = self.select(i)
            for j in range(self.move[i]):
                a0 = cn[0]
                b0 = dn[0]
                for k in range(27):  # 0-26
                    cn[k] = cn[k + 1]
                    dn[k] = dn[k + 1]
                cn[27] = a0
                dn[27] = b0
            # 56位 to 48位
            tem = cn + dn
            for m in range(0, 48):
                self.select(i).append(tem[self.pc_2[m] - 1])
            print("key", i + 1, self.select(i))

    def select(self, num):
        if num == 0: return self.k1
        if num == 1: return self.k2
        if num == 2: return self.k3
        if num == 3: return self.k4
        if num == 4: return self.k5
        if num == 5: return self.k6
        if num == 6: return self.k7
        if num == 7: return self.k8
        if num == 8: return self.k9
        if num == 9: return self.k10
        if num == 10: return self.k11
        if num == 11: return self.k12
        if num == 12: return self.k13
        if num == 13: return self.k14
        if num == 14: return self.k15
        if num == 15: return self.k16
