class Stack:
		def __init__(self):
			self.items = []

		def isEmpty(self):
			return self.items == []

		def push(self, item):
			self.items.insert(0,item)

		def pop(self):
			return self.items.pop(0)

		def peek(self):
			return self.items[0]

		def size(self):
			return len(self.items)

def dec2bin(decnum):
	s = Stack()
	binary = ''
	while decnum > 0:
		remainder = decnum % 2
		decnum = int(decnum/2)
		s.push(remainder)
	for i in range(s.size()):
		binary = binary + str(s.pop())

	return binary


print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))
