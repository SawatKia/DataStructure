class Stack:

    def __init__(self):
        self.items = []

    def data_since(self, i):
        return self.items[i:]

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


# Find the minimum element in list
def maxValIndex(list):
    n = len(list)
    if n > 1:
        maxVal, maxIdx = maxValIndex(list[:n - 1])
        if list[n - 1] > maxVal:
            return list[n - 1], n - 1
        else:
            return maxVal, maxIdx
    elif n == 1:
        return list[0], 0
    else:  # n < 1
        return None

def selectionsort(list, count = 0, sorted_L = [], maxval=None):
    n = len(list)
    if n == 1:
        j = len(sorted_L)-1
        while j >= 0:
            list.append(sorted_L[j])
            j-= 1
        return list
    # and place it at beginning
    maxval, maxidx = maxValIndex(list)
    count += 1
    last = list[n - 1]
    if maxval is not None:
        sorted_L.append(maxval)
    if last != maxval:
        list[n - 1],list[maxidx] = maxval,last
        i = len(sorted_L)-2
        while i >= 0:
            list.append(sorted_L[i])
            i-= 1
        print(f'swap {last} <-> {maxval} : {list}')
    sorted_list = (selectionsort(list[:n - 1], count, sorted_L, maxval))
    return sorted_list

inp = input('Enter Input : ').split()
for i in range(len(inp)):
    inp[i] = int(inp[i])
print(selectionsort(inp))
