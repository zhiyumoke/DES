"""
# Copyright (c) 2019 Ji Lei
# Created on 2019-3-27
# Author:Ji Lei
# Updeted on 2019-3-29
# Version 3.0
# Title: DES
"""
import ip
import Binary as bi
import function as f
import key
import math


def encode():
    input_type = input("——请选择明文类型 #字符串：1  #16进制：2——：")
    if input_type == '1':
        rawtext = input("——请输入明文——：")
        rawlist = list(rawtext)
        # counter为需要的des密码个数
        counter = math.ceil(len(rawtext) / 8)
        num = len(rawtext) % 8
    elif input_type == '2':
        rawtext = input("——请输入16进制明文——：")
        rawlist = list(rawtext)
        # counter为需要的des密码个数
        counter = 1
        num = 0
    else:
        print("wrong input")
    input_key = input("——请输入16进制密钥——：")

    # 补齐8个字符
    if num != 0:
        for i in range(8 - num):
            rawlist.append('\0')
        print("有", counter, "个DES", "最后一个DES补齐", num, "个'\\0'")

    k = 1
    key_class = key.KEY()
    key_64 = bi.key_con(input_key)
    key_class.key(key_64)

    for i in range(counter):
        # 内部为一次完整的des加密过程
        list_p = []
        # 字符型切片
        if input_type == '1':
            local_list = rawlist[(k - 1) * 8: k * 8]
            print("DES", k)
            print("明文：", local_list)
            list_p = bi.data_con(local_list)
            k = k + 1
        # 十六进制型切片
        elif input_type == '2':
            for j in rawlist:
                list_p = list_p + bi.sixteenb2two(j)
            print("DES", k)
            print("明文：", local_list)
        # ip置换
        l0, r0 = ip.ip(list_p)

        # 轮函数
        ln, rn = l0, r0
        for j in range(16):
            ln, rn = f.f(ln, rn, key_class.select(j))

        # ip-1置换
        ciphertext = ip.ip_t(rn + ln)
        ciphertext = bi.key_i(ciphertext)
        print("密钥：", str(input_key))
        print("16进制密文：", ''.join(ciphertext))


def decode():
    cipher = input("————请输入16进制密文————：")
    input_key = input("————请输入16进制密钥————：")
    # 密文处理
    list_c = []
    for i in cipher:
        list_c = list_c + bi.sixteenb2two(i)
    # 密钥处理
    key_class = key.KEY()
    key_64 = bi.key_con(input_key)
    key_class.key(key_64)

    # ip置换
    l0, r0 = ip.ip(list_c)

    # 轮函数
    ln, rn = l0, r0
    for j in range(16):
        ln, rn = f.f(ln, rn, key_class.select(15 - j))

    # ip-1置换
    plaintext = ip.ip_t(rn + ln)
    plaintext = bi.key_i(plaintext)
    print("密文:", cipher)
    print("密钥:", str(input_key))
    print("16进制明文:", ''.join(plaintext))


mode = int(input("——请选择DES模式 #加密：1  #解密：2——: "))
if mode == 1:
    encode()
elif mode == 2:
    decode()

"""
DES 1
明文： ['I', 'L', 'o', 'v', 'e', 'Y', 'o', 'u']
密钥： 1ABF458CD66D45AA
16进制密文： 524E2AB6B8C59975
"""
