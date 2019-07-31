
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def preOrderRecur(self,root):
        if root == None:
            return
        print(root.val,end=' ')
        self.preOrderRecur(root.left)
        self.preOrderRecur(root.right)
    def preOrderNoRecur(self,root):
        if root == None:
            return
        stack = []
        stack.append(root)
        while len(stack)>0:
            head = stack.pop()
            print(head.val,end=' ')
            if head.right !=None:
                stack.append(head.right)
            if head.left != None:
                stack.append(head.left)
        print()
    def inOrderRecur(self,root):
        if root == None:
            return
        self.inOrderRecur(root.left)
        print(root.val,end=' ')
        self.inOrderRecur(root.right)
    def inOrderNoRecur(self,root):
        if root == None:
            return
        stack = []
        cur = root
        while len(stack)!=0 or cur!=None:
            while cur!=None:
                stack.append(cur)
                cur = cur.left
            head = stack.pop()
            print(head.val,end=' ')
            cur = head.right
        print()
    def posOrderRecur(self,root):
        if root==None:
            return
        self.posOrderRecur(root.left)
        self.posOrderRecur(root.right)
        print(root.val,end=' ')
    ### 将先序变量改一改顺序 然后逆序输出 用栈实现
    def posOrderNoRecur1(self,root):
        if root == None:
            return
        stack1 = [root]
        stack2 = []
        while len(stack1)!=0:
            head = stack1.pop()
            stack2.append(head.val)
            if head.left != None:
                stack1.append(head.left)
            if head.right != None:
                stack1.append(head.right)
        while len(stack2)!=0:
            head = stack2.pop()
            print(head,end=' ')
        print()
    ### 单栈实现
    ### 用一个变量记录上一个打印出的节点
    def posOrderNoRecur2(self,root):
        if root == None:
            return
        stack = [root]
        h = root
        c = None
        while len(stack)!=0:
            c = stack[-1]
            ## c的左子树和右子树都没有处理
            if c.left!=None and c.left!=h and c.right!=h:
                stack.append(c.left)
            elif c.right!=None and h!=c.right:
                stack.append(c.right)
            else:
                print(c.val,end=' ')
                stack.pop()
                h = c
        print()
s = Solution()
### 初始化一个树
'''
      1
    2   3
  4  5  6  7
'''
nodes = []
for i in range(1,8):
    nodes.append(TreeNode(i))
n = len(nodes)
for i in range(n):
    if 2*i+1<n:
        nodes[i].left = nodes[2*i+1]
    if 2*i+2<n:
        nodes[i].right = nodes[2*i+2]

s.preOrderRecur(nodes[0])
print()
s.preOrderNoRecur(nodes[0])
s.inOrderRecur(nodes[0])
print()
s.inOrderNoRecur(nodes[0])
s.posOrderRecur(nodes[0])
print()
s.posOrderNoRecur1(nodes[0])
s.posOrderNoRecur2(nodes[0])