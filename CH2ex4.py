test_list = input("Enter Your List : ").split()
if len(test_list)<=2:
    print("Array Input Length Must More Than 2")
else:
    # initializing sum
    sum = 5
    # convert str to int
    for i in range(0, len(test_list)):
        test_list[i] = int(test_list[i])
    # using nested loops
    # 3 element sum
    res = []
    #check elem one by one
    for i in range(0, len(test_list)):
        for j in range(i + 1, len(test_list)):
            for k in range(j + 1, len(test_list)):
                if test_list[i] + test_list[j] + test_list[k] == sum:
                    temp = []
                    #add result to list
                    temp.append(test_list[i])
                    temp.append(test_list[j])
                    temp.append(test_list[k])
                    res.append(tuple(temp))
#answer method
    if len(res)==2:
        print('[', end='')
        for i in range(0, len(res)):
            print('[', end='')
            for j in range(0, len(res) + 1):
                print(str(res[i][j]), end='')
                if j != len(res):
                    print(', ', end='')
                else:
                    print(']', end='')
            if i != len(res) - 1:
                print(', ', end='')
            else:
                print(']')
    else:
        res.sort()
        print('[['+str(res[0][0])+', '+str(res[0][1])+', '+str(res[0][2])+']]')



