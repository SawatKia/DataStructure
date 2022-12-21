class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1]

    def push(self, tmp):
        self.items.append(tmp)

    def pop(self):
        tmp = self.items[-1]
        self.items.remove(tmp)
        return tmp


s = Stack()
open_paren = ["(", "{", "["]
close_paren = [")", "}", "]"]
paren = input("Enter expresion : ")
print(paren, end="")
for i in paren:
    if i in open_paren:
        s.push(i)
    elif i in close_paren:
        if s.size() == 0:
            print(" close paren excess")
            exit()
        elif open_paren.index(s.top()) != close_paren.index(i):
            print(" Unmatch open-close")
            exit()
        else:
            s.pop()
if s.size() != 0:
    print(" open paren excess   " + str(s.size()) + " : ", end="")
    t = ""
    while not s.isEmpty():
        t += s.top()
        s.pop()
    print(t[::-1])
else:
    print(' MATCH')