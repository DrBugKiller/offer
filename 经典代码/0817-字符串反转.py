# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 16:54
# @Author  : DrMa
'''
题目:
反转字符串, 不需要额外空间!
思路:
跟成对数组查找单身数类似的思路, 利用^异或运算,将收尾调换.
1.相同数异或等于0
2.任何数异或0等于本身.
例如:
a b c d e
a^e b c d e^(a^e)
-->a^e b c a
a^e^(a) b c a
-->e b c a 然后首尾两端缩进

'''
def reverseStr(s):
    if not s:
        return s
    ch = list(s)
    i , j = 0 , len(s)-1
    while i < j:
        #因为python中字符串不能直接^,所以用ord转为ascall码,然后chr(ASCLL)转为字符.
        ch[i] = chr(ord(ch[i]) ^ ord(ch[j]))
        ch[j] = chr(ord(ch[i]) ^ ord(ch[j]))
        ch[i] = chr(ord(ch[i]) ^ ord(ch[j]))

        # ch[i] = ch[i] ^ ch[j]  【错误的形式】
        # ch[j] = ch[i] ^ ch[j]
        # ch[i] = ch[i] ^ ch[j]
        i += 1
        j -= 1
    return "".join(ch)

s = 'abcde'
print(reverseStr(s))
def reverse(a):
    if not a:
        return a
    a_list=list(a)
    l_index=0
    r_index=len(a_list)-1
    while l_index<r_index:
        a_list[l_index]=chr( ord(a[l_index]) ^ ord(a[r_index])  )
        a_list[r_index]=chr( ord(a[l_index]) ^ ord(a[r_index])  )
        a_list[l_index]=chr( ord(a[l_index]) ^ ord(a[r_index])  )
        l_index+=1
        r_index-=1
    return "".join(a_list)
print(reverse('abn'))