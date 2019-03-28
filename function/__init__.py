import boxE as e
import boxS as s
import boxP as p


def f(ln_1=[], rn_1=[], kn=[]):  # 输入为32位
    rn = e.boxe(rn_1)  # 48位
    for i in range(48):
        rn[i] = xor(rn[i], kn[i])
    rn = s.boxs(rn)  # 32位
    rn = p.boxp(rn)
    for j in range(32):  # 32位异或
        rn[j] = xor(rn[j], ln_1[j])
    ln = rn_1
    return ln, rn


def xor(a, b):
    if a != b:
        return 1
    elif a == b:
        return 0
