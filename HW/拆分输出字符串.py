# 拆分输出字符串
# input_list=input().split(' ')
# N=int(input_list[0])
# str_list=input_list[1:]
str_list=['abc', '123124414','fjdsaf','    ']
N=4
out_list=[]

for i in range(N-1):
    for j in range(i+1,N):
        if len(str_list[i])<len(str_list[j]):
            temp=str_list[i]
            str_list[i]=str_list[j]
            str_list[j]=temp
for i in str_list:
    temp=i
    while len(temp)>8:
        out_list.append(temp[:8])
        temp=temp[8:]
    temp=temp+'0'*(8-len(temp))
    out_list.append(temp)
out_list.sort()
result=' '.join(out_list)
print(result)