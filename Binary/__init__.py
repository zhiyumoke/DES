# S盒用，行列坐标
def list2ten(input_6=[]):
    row = input_6[0] * 2 + input_6[5]
    col = input_6[1] * 8 + input_6[2] * 4 + input_6[3] * 2 + input_6[4]
    return row, col


# S盒用，十进制转二进制
def ten2two(num):
    if num == 0: return [0, 0, 0, 0]
    if num == 1: return [0, 0, 0, 1]
    if num == 2: return [0, 0, 1, 0]
    if num == 3: return [0, 0, 1, 1]
    if num == 4: return [0, 1, 0, 0]
    if num == 5: return [0, 1, 0, 1]
    if num == 6: return [0, 1, 1, 0]
    if num == 7: return [0, 1, 1, 1]
    if num == 8: return [1, 0, 0, 0]
    if num == 9: return [1, 0, 0, 1]
    if num == 10: return [1, 0, 1, 0]
    if num == 11: return [1, 0, 1, 1]
    if num == 12: return [1, 1, 0, 0]
    if num == 13: return [1, 1, 0, 1]
    if num == 14: return [1, 1, 1, 0]
    if num == 15: return [1, 1, 1, 1]


# main用，明文转
def data_con(input_list=[]):  # 在main内分割
    output_64 = []
    for i in input_list:
        num = ord(i)
        list_tem = list('{:08b}'.format(num))
        output_64 = output_64 + list_tem
    for i in range(64):
        output_64[i] = chr2num(output_64[i])
    return output_64


def chr2num(chra):
    if chra == '0':
        return 0
    elif chra == '1':
        return 1
    else:
        print("error")


# 16进制用，转成二进制数
def sixteenb2two(chr):
    if chr == '0': return [0, 0, 0, 0]
    if chr == '1': return [0, 0, 0, 1]
    if chr == '2': return [0, 0, 1, 0]
    if chr == '3': return [0, 0, 1, 1]
    if chr == '4': return [0, 1, 0, 0]
    if chr == '5': return [0, 1, 0, 1]
    if chr == '6': return [0, 1, 1, 0]
    if chr == '7': return [0, 1, 1, 1]
    if chr == '8': return [1, 0, 0, 0]
    if chr == '9': return [1, 0, 0, 1]
    if chr == 'A': return [1, 0, 1, 0]
    if chr == 'B': return [1, 0, 1, 1]
    if chr == 'C': return [1, 1, 0, 0]
    if chr == 'D': return [1, 1, 0, 1]
    if chr == 'E': return [1, 1, 1, 0]
    if chr == 'F': return [1, 1, 1, 1]


def key_con(input_list=[]):  # 在main内分割
    output_64 = []
    for i in input_list:
        output_64 = output_64 + sixteenb2two(i)
    return output_64


# 二进制数用，转成16进制数
def two2sixteen(child_list):
    if child_list == [0, 0, 0, 0]: return '0'
    if child_list == [0, 0, 0, 1]: return '1'
    if child_list == [0, 0, 1, 0]: return '2'
    if child_list == [0, 0, 1, 1]: return '3'
    if child_list == [0, 1, 0, 0]: return '4'
    if child_list == [0, 1, 0, 1]: return '5'
    if child_list == [0, 1, 1, 0]: return '6'
    if child_list == [0, 1, 1, 1]: return '7'
    if child_list == [1, 0, 0, 0]: return '8'
    if child_list == [1, 0, 0, 1]: return '9'
    if child_list == [1, 0, 1, 0]: return 'A'
    if child_list == [1, 0, 1, 1]: return 'B'
    if child_list == [1, 1, 0, 0]: return 'C'
    if child_list == [1, 1, 0, 1]: return 'D'
    if child_list == [1, 1, 1, 0]: return 'E'
    if child_list == [1, 1, 1, 1]: return 'F'


def key_i(input_list):
    output_16 = []
    for i in range(16):
        output_16.append(two2sixteen(input_list[i * 4:(i + 1) * 4]))
    return output_16
