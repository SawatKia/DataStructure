def sort(nums):
    new_lst = []
    for j in nums:
        j = int(j)
        new_lst.append(j)

    if len(new_lst) <= 1:
        return new_lst
    else:
        return (
            sort([i for i in new_lst[1:] if i > new_lst[0]])
            + [new_lst[0]]
            + sort([i for i in new_lst[1:] if i <= new_lst[0]])
        )


inp = input('Enter your List : ').split(',')
sorted = sort(inp)
print('List after Sorted : ',end='[')
for i in range(len(sorted)):
    if i!=len(sorted)-1:
        print(sorted[i],end=', ')
    else:
        print(sorted[i],end=']')

