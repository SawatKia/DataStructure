def smallestButGreaterThanX(list,x):
    for j in range(len(list)):
        if list[j] > x:
            return list[j]
    return print('No First Greater Value')

list1, list2 = input('Enter Input : ').split('/')
list1 = [int(i) for i in list1.split()]
list2 = [int(j) for j in list2.split()]
for i in range(len(list2)):
    num = smallestButGreaterThanX(sorted(list1),list2[i])
    if num != None:
        print(num)

