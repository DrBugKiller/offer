# N,M=list(map(int,input().split()))
N=4
M=3
x_start,y_start=0,1
x_end,y_end=0,1

# arr=[]
#
# for i in range(N):
#     arr.append(input().split())
arr=[['1', '2', '3'], ['3', '4', '5'], ['4', '5', '6'], ['566', '5', '7']]
path=[[True for j in range(M)]for i in range(N)]
