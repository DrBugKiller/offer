# import sys
# arrays=[]
# length_num=int(sys.stdin.readline())
# while True:
#     temp_str=sys.stdin.readline()
#     if temp_str=="\n":break
#     arrays.append(temp_str.strip('\n').split(','))
# #拿到数组

length_num=2
arrays=[[1,2,3],[4,5,6,6,7,7]]
arrays.pop(0)
print(arrays)
quit()
def temp_def2(arrays):
    len_arr=1
    output_arr=[]
    while len_arr>0:
        for i in arrays:
            for j in range(length_num):
                try:
                    temp=i.pop(0)
                    output_arr.append(int(temp))
                except:
                    pass
        len_arr=max([len(x) for x in arrays])
    return output_arr
print(temp_def2(arrays))

output_ar=[]
def temp_def(arrays):
    s=[]
    global  output_ar
    for i in arrays:
        if len(i)>length_num:
            output_ar.extend(i[:length_num])
            s.append(i[length_num:])
        else:
            output_ar.extend(i)
    return s
sheng_arr=arrays
while len(sheng_arr)>0:
    sheng_arr=temp_def(sheng_arr)
print(list(map(int,output_ar)))