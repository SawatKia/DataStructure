def isSorted(list):
    count = 0
    sorted = False
    for i in range(0,len(list)-1):
            if list[i]<list[i+1]:
                count += 1
            if count == len(list)-1:
                sorted = True
    return 'Yes' if sorted else 'No'


inp = input('Enter Input : ').split()
for i in range(len(inp)) :
    inp[i] = int(inp[i])

print(isSorted(inp))