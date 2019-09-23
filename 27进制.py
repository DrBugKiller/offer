# -*- coding: utf-8 -*-
# @Time    : 9/21/2019 9:12 PM
# @Author  : DrMa
# a = int(input())
s = '0123456789\'!@#$%^&*(){}\\<>?'
# rest = a
# ans = ''
# while rest >= 27:
#     value = rest // 27
#     ans += s[value]
#     rest = rest % 27
#     print(value, rest, ans)
# ans += s[rest]
# print(ans)
def conversion(n, d=27):
    res = []
    while (n // d >= 1):
        res.append(s[n % d])
        n = n // d
    if (n % d != 0):
        res.append(s[n%d])
    return ''.join(map(str,res[::-1]))
a=53
print(conversion(a,27))