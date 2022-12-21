class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

    def delete(root, data):
        if root is None:  # tree ว่่าง หรือ หาไม่เจอ
            print("Error! Not Found DATA")
            return None
        if data < root.data:  # ข่อมูลที่จะลบอยู่ซ้าย
            root.left = Node.delete(root.left, data)  # ลบข้อมูลฝั่งซ้าย
        elif data > root.data:  # ข่อมูลที่จะลบอยู่ขวา
            root.right = Node.delete(root.right, data)  # ลบข้อมูลฝั่งขวา
        else:  # หา data ที่จะลบเจอแล้ว
            if root.left is not None and root.right is not None:  # มีลูก 2
                cur = root.right
                while cur.left is not None:#find child right subtree
                    cur = cur.left
                root.data, cur.data = cur.data, root.data# สลับค่าระหว่างตัวที่จะลบกับ child right sub tree
                root.right = Node.delete(root.right, data)
            elif root.left is not None:
                return root.left
            elif root.right is not None:
                return root.right
            else:
                return None
        return root


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        elif self.root:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left is None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left

                else:
                    if cur.right is None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
        return self.root
    def delete(self, data):
        self.root = Node.delete(self.root, data)
        return self.root

        # if root is None:
        #     return print('Error! Not Found DATA')
        # if data < root.data:
        #     root.left = self.delete(root.left, data)#เลื่อนตัวชี้ไปโหนดซ้าย
        # elif data > root.data:
        #     root.right = self.delete(root.right, data)#เลื่อนตัวชี้ไปโหนดขวา
        # elif data == root.data:
        #     if root.left is None and root.right is None:
        #         root = None
        #     elif root.right.right is None:
        #         root.data = root.right
        #         root.right = None
        #     else:
        #         self.childRightSubtree(root, data)
        # else:#โหนดที่จะลบอยู่ที่โหนดนี้
        #     if not root.right:#ไม่มีลูกทางขวา
        #         return root.left #ให้เหลือแต่โหนดทางซ้าย
        #     if not root.left:#ไม่มีลูกทางซ้าย
        #         return root.right #ให้เหลือแต่โหนดทางขวา
        #     if root.left is not None and root.right is not None:#มีลูกทั้งสองฝั่ง
        #         self.childRightSubtree()
        #         # temp = root.right
        #         # small_val = temp.data
        #         # while temp.left:
        #         #     temp = temp.left
        #         #     small_val = temp.data
        #         # root.right = self.delete(root.right,root.data)
        # return self.root

def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)



tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
root = None
# for i in data:
#     temp = i.split()
#     num = int(temp[1])
#     if temp[0] == 'i':
#         print(f'insert {num}')
#         root = tree.insert(num)
#         printTree90(root)
#     elif temp[0] == 'd':
#         pass
for i in data:
    if i[0] == 'i':
        print(f'insert {i[2:]}')
        num = int(i[2:])
        root = tree.insert(num)
        printTree90(root)
    elif i[0] == 'd':
        print(f'delete {i[2:]}')
        num = int(i[2:])
        root = tree.delete(num)
        printTree90(root)

    # temp = i.split()
    # if temp[0] == 'i':
    #     #tree.insert(temp[1])
    #     print(f'insert {temp[1]}')
    #     printTree90(tree)
    # elif temp[0] == 'd':
    #     print(f'delete {temp[1]}')
    #     printTree90(tree.delete(temp[1]))
