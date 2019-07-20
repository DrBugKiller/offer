# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 10:58
# @Author  : DrMa
'''
题目3-特殊数组中重复的数字:
找出某特殊数组中重复的数字.在一个长度为n的数组里的所有数字都在0~n-1的范围内(特殊性)
例如, 输入{2,3,1,0,2,5,3},输出是2或者3.
'''







'''
题目4-特殊二维数组中的查找:
一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序(特殊性)。
请完成一个函数，输入这样一个二维数组和一个整数，判断数组中是否含有该整数。

思路:
 缩小范围的思路：从右上角或者左下角和目标int作比较，结合数组的特殊排序，分为三种情况，
右上角的数=目标数，直接return
'''
#这是自己的写的
class MySolution():
    def __init__(self,array_input,int_input):
        self.array_input=array_input
        self.int_input=int_input
    def judge(self):
        result=False
        raw_int = self.array_input[0][-1]
        try:#防治list index out of range
            if raw_int==self.int_input:
                result=True
            else:
                while self.int_input!=raw_int:
                    if self.int_input<raw_int:
                        self.array_input=[[y for y in x[:-1]]for x in self.array_input]#需改进
                        raw_int=self.array_input[0][-1]
                    if self.int_input>raw_int:
                        self.array_input=[[y for y in x]for x in self.array_input[1:]]#需改进
                        raw_int = self.array_input[0][-1]
                    if self.int_input==raw_int:
                        result=True
                        break
        except Exception as e:
            print(e)
            return result
        return result
array_input=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
a=MySolution(array_input,1)
print(a.judge())
#别人的，太简洁了
def array_Find(target, array):
    # write code here
    while len(array) > 0 and len(array[0]) > 0:#这个判断条件就是说数组不为空，行数>0并且列数>0
        print(array)
        if array[0][-1] == target:#先判断，满足就退出，两个return，只要return了一个，后边的就不会再次return
            return True
        elif array[0][-1] > target:
            # remove column
            array = [a[:-1] for a in array]#这句比我的简洁
        else:
            # remove row
            array = array[1:]#这句比我的简洁：把第一行删除，不删列，换句话说就是不取第0行，从第1行开始
    return False #这个return False是有前提的，就是前面并没有return任何东西。
target = 1
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(array_Find(target, array))


'''
题目7-重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None#None是因为left的类型也是TreeNode类型
        self.right = None
#这种表示方法都是孩子表示法,递归定义. self.left如果存在子树,那么就不是None,
#而是TreeNode(利用了递归).如果是叶节点
#这里的重建操作实际上是赋值操作
def reConstructBinaryTree(pre_order, in_order):
    if not pre_order or not in_order:
        return None
    #递归的结束条件
    #其实他俩共存共消. 只要有一个是空,另一个肯定也是空的. 比如说1的左子树:pre_inder{2,4,7} ,in_order{4,7,2}. 根节点是2,显然右子树
    #是不存在的,那么右子树的前序和中序都不存在.
    root = TreeNode(pre_order[0])#构建TreeNode类,并将val赋值成pre_order[0]

    pos = in_order.index(pre_order[0])#从中序遍历中拿到根节点所在的位置,然后

    root.left = reConstructBinaryTree(pre_order[1: pos+1], in_order[:pos])
    root.right = reConstructBinaryTree(pre_order[pos+1: ], in_order[pos+1: ])
    #我想问为什么pos+1如果超长度了不会报错?答案是不会报错,超过len(list)只会返回空的[]
    return root
a=reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
print(a.val)
print(a.left.val)
#这里需要注意下list的索引相关问题,因为涉及到递归的结束条件;
#详情看印象笔记中的"Python-list的index超过了list长度的两种情况":有冒号的情况下,如果某个索引值超出范围,并不会报错,返回一个空的list
#但是!如果是没有冒号,只定位一个,那么就会报错.


'''
题目8-二叉树的下一个结点:
思路:
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None#指向父节点的
#这个应该是双亲孩子表示法
def GetNext(pNode):
    # write code here
    if not pNode:#pNode是None就返回None
        return pNode
    if pNode.right:#if pNode.right!=None:如果一个节点有右子树,那么它的下一个节点是右子树中最左子节点
        temp=pNode.right
        while temp.left:
               temp=temp.left
        return temp
    #一个节点没有右孩子
    while pNode.parent:#一直到pNode是根节点,那么pNode.parent是None

        if pNode==pNode.parent.left:#如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。
            return pNode.parent
        #如果pNode不是左子树,往上走,一直找到左子树的跟节点.
        pNode=pNode.parent#如果pNode是根节点就结束
    return pNode
#pNode是TreeLinkNode类, 有4个属性值, 除了根节点是数值, 其他都是子树或者父母树类


'''
题目9：
用两个stack完成一个queue的功能
tips:
1.python自带的pop作用是删除最后(最右边)一个元素。
1.1在python中list的append相当于在栈中push，pop就是正常操作--把最后append的元素删除并返回
2.python的list中，如果当做栈来看的话，左边属于栈底，右边属于栈顶，append和pop都是在右边操作的。
3.此题的核心就是：push是利用stack1完成的，pop是利用stack1先把元素pop后push到stack2然后pop
'''
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop_(self):
        # return xx
        if len(self.stack2):#如果stack2有东西，直接把栈顶的pop出来即可
            return self.stack2.pop()
        while(self.stack1):#如果stack2空了，我们需要从stack1先pop出来然后push（append）到stack2中去
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
a=Solution()
for i in range(3):
    a.push(i)
print(a.pop_())
print(a.pop_())


'''
题目10-斐波那契数列:
1.青蛙跳台阶问题，花钱问题
2.求斐波那契数列的第n项
思路:
1.合理的数学建模，将问题转换成可递归公式
2.合理利用递归思想
3.考虑到效率问题，在递归的基础上进行拔升
'''
from  datetime import datetime
#100块钱，每次可以花1,2,3块钱，一共有多少种花法？
def mySolution(n):#简单，但是效率低
    if n==1:
        sum=1
    elif n==0:#边界值考虑清楚,如果有0元，那么0种花法
        sum=0
    elif n==2:#此处注意的是一定要把n=2,n=3考虑进去，因为此时它不满足sum = mySolution(n-1) + mySolution(n-2) + mySolution(n-3)
        sum = 2
    elif n==3:
        sum=4
    else:
        sum = mySolution(n-1) + mySolution(n-2) + mySolution(n-3)
    return sum
def mySolution_better(n):#效率极高
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    sum=0
    f_num=1
    s_num=2
    t_num=4
    for i in range(3,n):
        sum=f_num+s_num+t_num
        f_num=s_num
        s_num=t_num
        t_num=sum
    return sum
n=mySolution(3)
m=mySolution_better(100)
print(n)
print(m)
#斐波那契数列,但是效率极低
def mySolution_Fibonacci(n):
    if n==1:
        sum=1
    elif n==0:
        sum=0
    else :
        sum = mySolution_Fibonacci(n-1) + mySolution_Fibonacci(n-2)
    return sum
a=datetime.now()
print(mySolution_Fibonacci(35))
print(datetime.now()-a)
#斐波那契数列，效率极高，时间复杂度O(n)
def mySolution_Fibonacci_better(n):#0 1 1 2 3 5
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    #剩下的从3开始
    first=1
    second=1
    sum=0
    for i in range(2,n):
        sum=first+second
        first=second
        second=sum
    return sum
a=datetime.now()
print(mySolution_Fibonacci_better(35))
print(datetime.now()-a)


'''
Questions:
给定一个长度为n（整数）绳子，剪成m（整数）段，使得绳子的乘积最大。
Tips:
1.常规的动态规划O(n**2)时间复杂度，O(n)空间复杂度
2.贪婪算法，需要数学功底
'''
class Solution:
    def MaxProductAfterCut(self, n):
        # 动态规划
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        #剩下的是针对从n=4以后的
        products = [0] * (n + 1)
        products[0] = 0#这个0我觉得可以不要
        products[1] = 1
        products[2] = 2
        products[3] = 3

        for i in range(4, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if product > max:#遍历1~（i除以2向下取整），对应f
                    max = product
            products[i] = max
        # print(products)
        return products[n]

    def MaxProductAfterCut2(self, n):
        # 贪婪算法
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        timesOf3 = n // 3
        if n - timesOf3 * 3 == 1:
            timesOf3 -= 1

        timesOf2 = (n - timesOf3 * 3) // 2
        return (3 ** timesOf3) * (2 ** timesOf2)
print(Solution().MaxProductAfterCut(8))
print(Solution().MaxProductAfterCut(10))
# print(Solution().NumberOf1(0))
print(Solution().MaxProductAfterCut2(8))
print(Solution().MaxProductAfterCut2(10))