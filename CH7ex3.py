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
        if self.root is None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left is None:
                        cur.left = Node(data)
                        break
                    cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = Node(data)
                        break
                    cur = cur.right
        return self.root

    def treeHeight(self, root):
        cur = root
        H_left = H_right = 0
        if cur is None:
            return -1
        if cur.left is not None:
            H_left = self.treeHeight(cur.left)
        if cur.right is not None:
            H_right = self.treeHeight(cur.right)
        H = max(H_left,H_right)
        if cur != self.root:
            H += 1
        return H
        # cur = self.root
        # while cur.right is not None:
        #     H_Right += 1
        #     if cur.left is None:
        #         cur =cur.right
        # if H_Left > H_Right:
        #     return H_Left
        # elif H_Right > H_Left:
        #     return H_Right
        # elif H_Right == H_Left:
        #     return H_Right
        # else:
        #     return 0

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)



def compare(root, k,count=0):
    cur = root
    if cur is not None:
        if cur.data <= k:
            count += 1
        if cur.left is not None:
            count = compare(cur.left,k,count)
        if cur.right is not None:
            count = compare(cur.right,k,count)
        return count


inp,k = input('Enter Input : ').split('/')
T = BST()
k = int(k)
for i in inp.split():
    root=T.insert(int(i))
T.printTree(root)
print('--------------------------------------------------')
print(compare(root,k))