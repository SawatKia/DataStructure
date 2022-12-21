stack = []

elem = input("Enter Input : ").split(",")

for i in elem :
    temp=i.split()

    if temp[0]=='A':
        stack.append(temp[1])

        print("Add = "+str(temp[1])+" and Size = "+str(len(stack)))
    else :
        if len(stack) == 0:
            print("-1")
        else:
            temp=stack[-1]
            lenght = len(stack)
            stack.pop()
            print("Pop = " + str(temp) + " and Index = " + str(lenght - 1))
if len(stack) == 0 :
    print("Value in Stack = Empty")
else:
    print("Value in Stack = ",end='')
    for i in stack:
        print(str(i),end=' ')


