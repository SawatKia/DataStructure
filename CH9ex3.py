# def insertionSort(list,n):
#     if (n <= 1):
#         return
#     insertionSort(list,n-1)
#     value = list[n-1]
#     pos = n-2
#     while pos >= 0 and list[pos] > value:
#         list[pos+1] = list[pos]
#         #print(f'insert {value} at index {pos} :', end=' ')
#         pos -= 1
#     list[pos+1] = value
#     #print(list)
#     return list

def iter_insertionSort(list, cutted_l, n, sorted_l = [], recur = False,count = 1):
    pos = 0
    if count == 1:#ถ้าเป็นครั้งแรก
        sorted_l.append(list.pop(0))#ให้แยกเป็น2ลิสคือ1.ลิสของตัวเลขแรก(ลิสที่เรียงแล้ว)2.ลิสของตัวเลขที่เหลือ(ยังไม่เรียง)
        count += 1
        cutted_l.pop(0)
        iter_insertionSort(list, cutted_l, n, sorted_l, True, count)
        if len(sorted_l) == n:
            return sorted_l
    if count != 1:#ถ้าไม่ใช่ครั้งแรก
        if len(list) != n and len(sorted_l) == 1 and recur:
            if len(list) > 0:
                count += 1
                iter_insertionSort(list[:len(list)-1], cutted_l, n-1, sorted_l, True, count)#เรียกซ้ำส่งพารามีเตอร์โดยตัดตัวสุดท้ายออกทีละตัวและrecur=true
        if len(list)!= n:#ถ้าเป็นการrecurและ len(list) != n
            if len(list) > 0:
                # if len(sorted_l) > 1:  # ถ้า len(sorted_l) > 1
                #     iter_insertionSort(list, n,sorted_l[:len(list) - 1, True, count])  # เรียกซ้ำตัด sort_l ตัวท้ายสุดออกทีละตัว
                if len(sorted_l) == 0:  # ถ้า len(sorted_l) = 0
                    return 0
                if list[-1] < sorted_l[-1]:  # list[0] < sorted_l[0]
                    count += 1
                    if len(sorted_l) != 0:
                        #pos = iter_insertionSort(list, cutted_l, n+1 , sorted_l[:len(sorted_l)-1], False, count)
                        pos = idxGreaterthanX(sorted_l,list[-1])
                    if pos >= 0:
                        sorted_l.insert(pos,list[-1])
                        cutted_l.pop(0)
                        printstatus(list.pop(-1), pos, sorted_l, cutted_l)
                elif list[-1] > sorted_l[-1]:
                    pos = len(sorted_l)
                    sorted_l.append(list[-1])
                    cutted_l.pop(0)
                    printstatus(list.pop(-1),len(sorted_l)-1,sorted_l,cutted_l)
            return pos#return

def idxGreaterthanX(list, num):
    index = 0
    if len(list) == 0:
        return 0
    if list[-1] < num:
        index = len(list)
    elif len(list) > 0:
        index = idxGreaterthanX(list[:len(list)-1],num)
    return index


def printstatus(val, idx, sorted, rest):
    print(f'insert {val} at index {idx} : {sorted}',end=' ')
    if len(rest) != 0:
        print(f'{rest}')

inp = input("Enter Input : ").split()
l,sorted_list = [],[]
for i in inp:
    l.append(int(i))
#print(insertionSort(inp,len(inp)))
#print(__iter_insertionSort__(l,len(l)))
#recInsertionSort(l, [], len(l))
cutted = list(l)
sorted_list = iter_insertionSort(l, cutted, len(l))
if len(sorted_list) > 0:
    print('\nsorted')
print(f'{sorted_list}')