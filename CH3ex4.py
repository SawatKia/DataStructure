class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return 1

    def isEmpty(self):
        return len(self.items) == 0


stack = Stack()
stack_temp = Stack()
list = input('Enter Input : ').split(",")
last_number = None
lowless_number = None
counting = 0
for type_and_height in list:
    type_and_height = type_and_height.split(" ")
    type = type_and_height[0]
    if type == 'A':
        current_number = type_and_height[1]
        current_number = int(current_number)
        last_number = current_number
        stack.push(current_number)
    elif type == 'B':
        if stack.size() > 0:
            for i in range(0, stack.size()):
                if lowless_number == None:
                    lowless_number = stack.pop()
                    stack_temp.push(lowless_number)
                    counting += 1
                elif lowless_number < stack.peek():
                    counting += 1
                    lowless_number = stack.pop()
                    stack_temp.push(lowless_number)

                elif lowless_number >= stack.peek():
                    stack_temp.push(stack.pop())
            for i in range(0, stack_temp.size()):
                stack.push(stack_temp.pop())
                # stack_temp.push(stack.pop())
        print(counting)
        counting = 0
        lowless_number = None
    # elif type == 'S':
    #     for i in range(0,stack.size()):
    #         number = stack.pop()
    #         if number % 2 == 1:
    #             number += 2
    #             stack_temp.push(number)
    #         elif number % 2 == 0:
    #             number -= 1
    #             stack_temp.push(number)
    #     for i in range(0,stack_temp.size()):
    #         stack.push(stack_temp.pop())
