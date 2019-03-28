"""
# Copyright (c) 2019 Ji Lei
# Created on 2019-3-27
# Author:Ji Lei
# Updeted on 2019-3-28
# Version 2.0
# Title: DES
"""
import ip
import Binary as bi
import function as f
import key
import math


class des():
    input_type = input("————please choose plaintext type ## 1：str ##2:sixteen-binary ————： ")
    if input_type == '1':
        rawtext = input("please input plaintext: ")
        rawlist = list(rawtext)
        # counter为需要的des密码个数
        counter = math.ceil(len(rawtext) / 8)
        num = len(rawtext) % 8
    elif input_type == '2':
        rawtext = input("please input 16-binary plaintext: ")
        rawlist = list(rawtext)
        # counter为需要的des密码个数
        counter = 1
        num = 0
    else:
        print("wrong input")
    rawkey = input("please input 16-binary key: ")

    # 补齐8个字符
    if num != 0:
        for i in range(8 - num):
            rawlist.append('\0')
    print("有", counter, "个DES", "最后一个DES补齐", num, "个'\\0'")

    k = 1
    key_class = key.KEY()
    key_64 = bi.key_con(rawkey)
    key_class.key(key_64)

    for i in range(counter):
        # 内部为一次完整的des加密过程
        list = []
        # 字符型切片
        if input_type == '1':
            temlist = rawlist[(k - 1) * 8: k * 8]
            print("DES", k)
            print("plaintext", temlist)
            list = bi.data_con(temlist)
            print("list", list)
            k = k + 1
        # 十六进制型切片
        elif input_type == '2':
            for j in rawlist:
                list = list + bi.sixteenb2two(j)
            print("DES", k)
            print("plaintext", list)
        # ip置换
        l0, r0 = ip.ip(list)

        # 轮函数
        ln, rn = l0, r0
        for j in range(16):
            ln, rn = f.f(ln, rn, key_class.select(j))

        # ip-1置换
        ciphertext = ip.ip_t(rn + ln)
        print("ciphertext", ciphertext)
        ciphertext = bi.key_i(ciphertext)
        print("16-binary ciphertext", ciphertext)


'''
DES 1
plaintext ['i', 'm', 'j', 'i', 'l', 'e', 'i', '\x00']
list [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
ciphertext [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0]
16-binary ciphertext ['B', '2', '5', 'F', '8', '2', '1', '2', 'E', '9', 'F', '0', '8', 'D', 'D', '2']'''

'''
DES 1
plaintext ['i', 'l', 'o', 'v', 'e', 'y', 'o', 'u']
list [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
ciphertext [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
16-binary ciphertext ['2', '1', '9', '4', '5', '2', '0', '0', 'C', '6', '8', 'E', '0', '6', 'A', '5']
'''

'''
DES 1
plaintext [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
ciphertext [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
16-binary ciphertext ['8', '5', 'E', '8', '1', '3', '5', '4', '0', 'F', '0', 'A', 'B', '4', '0', '5']
'''
