class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, key, value, tablesize, maxCollis, table):
        self.data = Data(key, value)
        if len(table) == 0:
            self.table = [None]*tablesize
        else:
            self.table = table
        self.tableSize = tablesize
        self.maxCollis = maxCollis

    def __str__(self):
        for i in range(1,len(self.table)+1):
            print(f'#{i}	',end='')
            if self.table[i-1] is not None:
                print(f'({self.table[i-1]})')
            else:
                print(f'{self.table[i-1]}')
        print('---------------------------')

    def isfull(self):
        count = 0
        for i in self.table:
            if i is not None:
                count += 1
        if count == len(self.table):
            return True
        else:
            return False

    def hashing(self):
        index = sum(map(ord,self.data.key))%self.tableSize
        #print(f'sum ascii of "{self.data.key}" and value to store "{self.data.value}" : {sum(map(ord,self.data.key))}')
        #print(f'----calculating index---- \n{sum(map(ord,self.data.key))} % {self.tableSize} == index : {index}')
        return index

    def insert(self, index):
        if not self.isfull():
            const_idx = index
            #print(f'insert : {value} at {index}')
            if self.table[index] is None :
                self.table[index] = self.data.key + ', '+ self.data.value
            else:
                i = 1
                #print(f'self.table[index] : {self.table[index]}')
                while self.table[index] is not None and i <= self.maxCollis:
                    print(f'collision number {i} at {index}')
                    index = int(const_idx + i**2)
                    i += 1
                    if index >= len(self.table):
                        index %= tableSize

                if i-1 == self.maxCollis:
                    print('Max of collisionChain')
                    self.__str__()
                    return
                self.table[index] = self.data.key + ', '+ self.data.value
            self.__str__()
        elif self.isfull():
            print('This table is full !!!!!!')
            return
        else:
            return

    def lenght(self):
        count = 0
        for i in self.table:
            if i is not None:
                count += 1
        return count


    # def isDuplicate(self):
    #     duplicate = False
    #     for i in self.table:
    #         if i is not None:
    #             text = i.split(', ')
    #             if text[1] == self.data.value:
    #                 duplicate = True
    #                 break
    #             else:
    #                 duplicate = False
    #     return duplicate


print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
tableSize, MaxCollis = [int(i) for i in inp[0].split()]
data = inp[1].split(',')
table = []
count = 0
for i in range(len(data)):
    key,value = data[i].split()
    hash = Hash(key, value, tableSize, MaxCollis, table)
    #print('1')
    if not hash.isfull():
        hash.insert(hash.hashing())
        table = hash.table
    if hash.isfull() and count == 0:
        count+=1
        print('This table is full !!!!!!')
