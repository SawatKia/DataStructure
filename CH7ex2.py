# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def __str__(self):
#         return str(self.data)
#
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             cur = self.root
#             while True:
#                 if data < cur.data:
#                     if cur.left is None:
#                         cur.left = Node(data)
#                         break
#                     cur = cur.left
#                 else:
#                     if cur.right is None:
#                         cur.right = Node(data)
#                         break
#                     cur = cur.right
#         return self.root
#
#         def treeHeight(self, root):
#             cur = self.root
#             if cur is None:
#                 return 0
#
#         # cur = self.root
#         # while cur.right is not None:
#         #     H_Right += 1
#         #     if cur.left is None:
#         #         cur =cur.right
#         # if H_Left > H_Right:
#         #     return H_Left
#         # elif H_Right > H_Left:
#         #     return H_Right
#         # elif H_Right == H_Left:
#         #     return H_Right
#         # else:
#         #     return 0
#
#     def printTree(self, node, level=0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)
#
#
# inp = input('Enter Input : ').split()
# T = BST()
# for i in inp:
#     root=T.insert(i)
# print(f'Height of this tree is : {T.treeHeight(root)}')
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BST._insert(self.root, data)
        return self.root

    def _insert(root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = BST._insert(root.left, data)
        else:
            root.right = BST._insert(root.right, data)
        return root

    def getHeight(root: Node):
        if root is None:
            return -1
        return 1 + max(BST.getHeight(root.left), BST.getHeight(root.right))


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is :", BST.getHeight(root))