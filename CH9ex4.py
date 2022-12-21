def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return array

def median(list):
    list = insertionSort(list)
    index = ((len(list)+1)/2)-1
    if len(list) == 1:
        return list[int(index)]
    elif not index.is_integer():
        i = int(index - 0.5)
        j = int(index + 0.5)
        return (list[i]+list[j])/2
    else:
        return list[int(index)]

def printListMed(list,med):
    print(f'list = {list} : median =',end=' ')
    print('%.1f' % med)

list = []
unsorted_L = []
inp = input('Enter Input : ').split()
inp = [int(i) for i in inp]
for i in inp:
    list.append(i)
    unsorted_L.append(i)
    med = median(list)
    printListMed(unsorted_L,med)



