# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 20:46
# @Author  : DrMa
'''
题目: 请实现一个函数, 把字符串中的每个空格替换成"%20".
例如, 输入"We are happy.",则输出"We%20are%20happy."
思路: 从前往后,慢,时间复杂度为O(n^2), 因为部分字符会重复移动.
      从后往前,快,时间复杂度为O(n), 所有字符只会移动一遍.
'''
def replace_op(a,str_blk,str_obj):
    '''
    a:原始字符串;    str_blk:空格;   str_obj:要替换成的字符串
    '''
    a=[x for x in a]#转换为list
    num_blk=a.count(str_blk)#空格的数量
    len_diff=(len(str_obj)-len(str_blk))*num_blk#新字符串和原字符串的长度差;
    org_len=len(a)#原字符串长度
    new_len=org_len+len_diff#新字符串长度
    index_org=org_len-1#源字符串起始index
    index_new=new_len-1#新字符串起始index
    a+=[None]*len_diff #这句话是核心
    while index_org>=0 and index_org<index_new:#注意条件
        if a[index_org]==str_blk:
            for i in str_obj[::-1]:#倒序插入目标字符串.
                a[index_new]=i
                index_new-=1#每复制一个str_obj中的字符,index_new减1
            index_org-=1#新字符串都替换完了index_org才减1
        else:
            a[index_new]=a[index_org]
            index_org-=1
            index_new-=1
    return ''.join(a)
if __name__=='__main__':
    a='We are happy.'
    print(replace_op(a,' ','##123'))
