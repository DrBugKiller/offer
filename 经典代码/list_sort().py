# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 10:01
# @Author  : DrMa
#介绍list.sort()的高端操作，尤其是需要有自定义排序需求的时候
org_list=['abcdefd','12345','ABCDEFGHJK']
len_list=list(map(len,org_list))
list_out=list(zip(org_list,len_list))
print('原始字符串：\n',list_out)
def takeindex_elem(elem):
    '''
    此函的输入是合成后的list中的子元素element，
    返回的是自己指定的---子元素的某个子元素，此处是返回elem的第二个elem[1]
    '''
    return elem[1]
list_out.sort(key=takeindex_elem,reverse=True)
print('根据字符串长度排序，降序：\n',list_out)
list_out.sort(key=lambda s:s[0],reverse=True)#用lambda更简洁一些
print('根据字符串自身排序，降序：\n',list_out)