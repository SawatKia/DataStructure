class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self.__str__()

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:  # if linked list is empty, then the new_node is head
            self.head = new_node
        else:
            cur = self.head  # define
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            new_node.previous = cur
            return

    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        new_node.previous = None
        if self.isEmpty() != True:
            self.head.previous = new_node
        self.head = new_node

    def insert(self, pos, item):
        if self.size() == 0:
            self.append(item)
        else:
            new_node = Node(item)
            if pos >= self.size():
                self.append(item)
            elif pos < (self.size()*-1):
                self.addHead(item)
            elif pos == 0:
                cur = self.head
                new_node.next = cur
                new_node.previous = None
                self.head = new_node
            elif pos == -1:
                cur = self.head
                while cur.next.next != None:
                    cur = cur.next
                new_node.next = cur.next
                new_node.previous = cur
                cur.next = new_node
            elif pos <= 0:
                cur = self.head
                index = self.size()*(-1)
                while cur.next != None and index != pos-1:
                    cur = cur.next
                    index += 1
                new_node.next = cur.next
                new_node.previous = cur
                cur.next = new_node

            else:
                # traverse to target position
                cur = self.head
                count = 0
                while count != pos:
                    cur = cur.next
                    count += 1
                    if count == pos - 1:
                        new_node.next = cur.next
                        cur.next = new_node
                new_node.previous = cur.previous

    def search(self, item):
        found = 0
        count = 0
        cur = self.head
        while count <= self.size()-1:
            count += 1
            if cur.value == item:
                found = 1
            cur = cur.next
        if found == 0:
            return 'Not Found'
        else:
            return 'Found'

    def index(self, item):
        idx = 0
        found = -1
        cur = self.head
        while idx <= self.size()-1:
            idx += 1
            if cur.value == item:
                idx -= 1
                found = 0
                return idx
            cur = cur.next

        return found# if not match any elem

    def size(self):
        if self.head != None:
            count = 1
            cur = self.head
            while cur.next != None:
                cur = cur.next
                count += 1
            return count
        else:
            return 0

    def pop(self, pos):
        if pos < 0 or pos >= self.size():
            return "Out of Range"
        if pos == 0 and self.size() > 0:
            self.head = self.head.next
            return "Success"
        else:
            cur = self.head
            for i in range(0, pos):
                cur = cur.next
            cur.next = cur.next.next
            if i+1 == pos:
                return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())

