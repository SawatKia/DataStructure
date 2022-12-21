# def median(list):
#     index = ((len(list)+1)/2)-1
#     if len(list) == 1:
#         return list[int(index)],int(index)
#     elif not index.is_integer():
#         i = int(index - 0.5)
#         j = int(index + 0.5)
#         return (list[i]+list[j])/2,(i+j)/2
#     else:
#         return list[int(index)],int(index)

def MedIdx(list):
    if len(list) == 1:
        return 0
    elif len(list) % 2 == 1:
        return int((len(list) - 1) / 2)
    elif len(list) % 2 == 0:
        return int((len(list) / 2) - 1)

def bi_search(i, lenght, list, key):
    found = False
    if lenght > 0:
        idx = MedIdx(list)
        if key == list[idx]:
            return True
        elif key != list[idx]: #not found that key
            if lenght != 1:
                if key < list[idx]:
                    found = bi_search(i+1, len(list[:idx]), list[:idx], key)
                    #return False
                elif key > list[idx]:
                    found = bi_search(i + 1, len(list[idx+1:]), list[idx+1:], key)
                    #return False
            else:
                return False
            #return False
    return found



inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
