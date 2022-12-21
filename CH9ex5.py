def bubleSorted(l) :
    n = len(l) - 1
    for i in range(n + 1):
        for j in range(0, n-i):
            if l[j] > l[j + 1] :
                l[j], l[j + 1] = l[j + 1], l[j]


def subset(input):
    if input == []:
        return [[]]
    else:
        a = subset(input[1:])
        return a + [[input[0]] + b for b in a]

def bubleSortedList(l) :
    n = len(l) - 1
    for i in range(n + 1):
        for j in range(0, n-i):
            if len(l[j]) > len(l[j + 1]) :
                l[j], l[j + 1] = l[j + 1], l[j]

def sum(arr):
    x = 0
    for i in arr :
        x += i
    return x

def allSubsetSort(PA) :
    bubleSorted(PA)
    bubleSortedList(PA)
    return PA


inp = input("Enter Input : ").split("/") # result / subset that sum equel result
result = int(inp[0])
A = [eval(i) for i in inp[1].split()]
bubleSorted(A)
PA = subset(A)
s = 0
for item in allSubsetSort(PA):
    if sum(item) == result :
        print(item)
        s += 1

if s == 0 : print("No Subset")