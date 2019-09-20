# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 19:51
# @Author  : DrMa
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None#None是因为left的类型也是TreeNode类型
        self.right = None

# T58
class TreeLinkNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    '''
    所有的def
    '''
    '''
    7 重建二叉树
    输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
    假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
    '''
    def reConstructBinaryTree(self, pre_order, in_order):
        if not pre_order or not in_order:
            return None
        #其实他俩共存共消. 只要有一个是空,另一个肯定也是空的. 比如说1的左子树:pre_inder{2,4,7} ,in_order{4,7,2}. 根节点是2,显然右子树
        #是不存在的,那么右子树的前序和中序都不存在.
        root = TreeNode(pre_order[0])#构建TreeNode类,并将val赋值成pre_order[0]
        pos = in_order.index(pre_order[0])#从中序遍历中拿到根节点所在的位置,然后
        # print(pre_order[1: pos+1], in_order[:pos])
        # print(pre_order[pos+1: ], in_order[pos+1: ])
        root.left = self.reConstructBinaryTree(pre_order[1: pos+1], in_order[:pos])
        root.right = self.reConstructBinaryTree(pre_order[pos+1: ], in_order[pos+1: ])
        #我想问为什么pos+1如果超长度了不会报错?答案是不会报错,超过len(list)只会返回空的[]

        return root
    '''
    8 二叉树的下一个节点
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
    '''
    def GetNext(self, pNode):
        if not pNode:
            return None
        # 右节点不为空：返回右节点的最左节点
        if pNode.right:
            tmp = pNode.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        else:
            if not pNode.next:
                return None
            elif pNode.next.left == pNode:
                return pNode.next
            else:
                if pNode.next.next.left == pNode.next:
                    return pNode.next.next
                else:
                    return None
    '''
    26 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
    递归
    '''
    def hasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False

        result = False

        if(pRoot1.val == pRoot2.val):
            result =  self.isSubtree(pRoot1, pRoot2)

        if not result:
            result = self.isSubtree(pRoot1.left, pRoot2)

        if not result:
            result = self.isSubtree(pRoot1.right, pRoot2)
        return result

    def isSubtree(self, p1, p2):
        if not p2:
            return True
        if not p1:
            return False
        if p1.val != p2.val:
            return False
        return self.isSubtree(p1.left, p2.left) and self.isSubtree(p1.right, p2.right)
    '''
    27：二叉树的镜像
    '''
    def mirror(self, root):
        if not root:
            return root
        root.left, root.right = root.right, root.left#python还能这么玩?
        self.mirror(root.left)
        self.mirror(root.right)
    '''
    32 从上往下打印二叉树
    '''
    '''
    34 二叉树中和为某一值的路径
    输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
    路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
    (注意: 在返回值的list中，数组长度大的数组靠前)
    '''
    def findPath(self, root, expectNumber):
        if not root:
            return []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        left = self.findPath(root.left, expectNumber - root.val)
        right = self.findPath(root.right, expectNumber - root.val)
        # for i in left + right:
        #     result.append([root.val] + i)
        result = [root.val] + left + right
        return result
    '''
    55 二叉树的深度
    输入一棵二叉树，求该树的深度。
    从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
    '''
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left+1, right+1)
    '''
    28 对称的二叉树
    请实现一个函数，用来判断一颗二叉树是不是对称的。
    注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
    '''
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        else:
            return self.isSameTree(pRoot.left, pRoot.right)

    def isSameTree(self, p, q):
        # 如果两个都空
        if not p and not q:
            return True
        # 如果两个有一个为空
        if not p or not q:
            return False
        # 如果两个都不为空
        if p and q and p.val == q.val:
            l = self.isSubtree(p.left, q.right)
            r = self.isSubtree(p.right, q.left)
            return l and r
    '''
    60 把二叉树打印成多行
    从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
    '''
    # 用一个队列来保存将要打印的结点。为了把二叉树的每一行单独打印到一行里，
    # 我们需要两个变量：一个变量表示在当前的层中还没有打印的结点数，另一个变量表示下一次结点的数目。
    # 队列：
    # 每次打印一个结点的时候，如果该结点有子结点，则把该结点的子结点放到队列末尾。
    # 接下来到队列头部取出最早进入队列的结点，重复前面的打印操作，直至队列中所有结点都被打印出来为止。
    def Print(self, pRoot):
        if not pRoot:
            return []
        res, tree = [], [pRoot]
        while tree:
            row, subTree = [], []
            for item in tree:
                row.append(item.val)
                if item.left:
                    subTree.append(item.left)
                if item.right:
                    subTree.append(item.right)
            res.append(row)
            tree = subTree
        return res
    '''
    61 按之字形顺序打印二叉树
    '''
    # 按之字形顺序打印二叉树需要两个栈。我们在打印某一行结点时，把下一层的子结点保存到相应的栈里。
    # 如果当前打印的是奇数层，则先保存左子结点再保存右子结点到一个栈里；
    # 如果当前打印的是偶数层，则先保存右子结点再保存左子结点到第二个栈里。
    # 分析题意：当打印奇数行时，按照从左到右的顺序打印，当打印偶数行时，要按照从右往左相反的方向打印，
    # 这样的结构很自然想到用栈来实现，但我们需要创建两个栈，来区分偶数行和奇数行的情况。
    # 当为奇数行时，需要从右到左入栈，从左到右出栈，偶数行相反。
    # https: // blog.csdn.net / shizhengxin123 / article / details / 79424034
    def Print_(self, pRoot):
        if not pRoot:
            return []
        result, nodeStack = [], [pRoot]
        times = 0
        while nodeStack:
            times += 1
            res, nextStack = [], []
            for item in nodeStack:
                res.append(item.val)
                if item.left:
                    nextStack.append(item.left)
                if item.right:
                    nextStack.append(item.right)
            if times % 2 == 0:
                res = res[::-1]

            nodeStack = nextStack
            result.append(res)
        return result
    '''
    37 序列化二叉树
    请实现两个函数，分别用来序列化和反序列化二叉树
    '''
    # https: // blog.csdn.net / u010005281 / article / details / 79787278
    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        list = s.split(',')
        return self.deserializeTree(list)

    def deserializeTree(self, list):
        if not list:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.deserializeTree(list)
            root.right = self.deserializeTree(list)
        return root
    '''
    平衡二叉树
    输入一棵二叉树，判断该二叉树是否是平衡二叉树
    '''
    # pdf
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        # 对左右两边同时递归
        if abs(self.treeDepth(pRoot.left) - self.treeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def treeDepth(self, pRoot):
        if not pRoot:
            return 0
        # 二叉树的后序遍历
        left = self.treeDepth(pRoot.left)
        right = self.treeDepth(pRoot.right)
        return max(left+1, right+1)  # 返回当前树深


s=Solution()
root=s.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])


temp=[1,2,3]
print(temp[3:])
print(temp[2:7])


# print(root.left.val)
# print(root.right.val)

