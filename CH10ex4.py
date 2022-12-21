class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


def ascii(data):
    x = 0
    for i in data:
        x += ord(i)
    return x


def f(i):
    return i * i


def isPrime(n, i=2):
    # Base cases
    if (n <= 2):
        return True if (n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    # Check for next divisor
    return isPrime(n, i + 1)


def toPrime(num, b):
    if isPrime(num):
        return b
    else:
        return toPrime(num + 1, b + 1)


class hash:
    # Code Here
    def __init__(self, maxSize, maxCollision, Threshold):
        self.table = [None] * maxSize
        self.size = 0
        self.temp = []
        self.maxSize = maxSize
        self.maxCollision = maxCollision
        self.Threshold = Threshold
        print("Initial Table : ")
        self.printTable()
        print("----------------------------------------")

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size >= self.maxSize

    def add(self, data, i=0):
        index = (data + f(i)) % self.maxSize  # i คือจำนวนการชน
        percent = int(self.maxSize * (Threshold / 100))
        if self.size >= percent:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            self.add(data, 0)
        elif self.isEmpty():
            self.table[index] = data
            self.size += 1
            self.temp.append(data)
        elif self.table[index] == None and i < self.maxCollision:
            self.table[index] = data
            self.size += 1
            self.temp.append(data)
        elif self.table[index] != None and i < self.maxCollision:
            print("collision number {0} at {1}".format(i + 1, index))
            self.add(data, i + 1)
        elif i >= self.maxCollision:
            print("****** Max collision - Rehash !!! ******")
            self.rehash()
            self.add(data, 0)

    def rehash(self):
        b = toPrime(self.maxSize * 2, 0)
        self.maxSize = (2 * self.maxSize) + b
        self.table = [None] * self.maxSize
        self.size = 0
        temp = self.temp
        self.temp = []
        for i in temp:
            self.add(i)

    def printTable(self):
        for i in range(self.maxSize):
            print("#{0}	{1}".format(i + 1, self.table[i]))

    def check(self, data):
        status = False
        for i in self.table:
            if i == data:
                status = True
                break
        return status


inp = input(" ***** Rehashing *****\nEnter Input : ").split("/")
detail = inp[0].split()
tableSize, maxCollision, Threshold = int(detail[0]), int(detail[1]), int(detail[2])
data = inp[1].split()
h = hash(tableSize, maxCollision, Threshold)
for i in data:
    if int(i) >= 0 and Threshold >= 0 and Threshold <= 100 and h.check(int(i)) != True and maxCollision >= 0:
        print("Add : {0}".format(i))
        h.add(int(i))
        h.printTable()
        print("----------------------------------------")



