class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def Enqueue(self, value):
        self.items.append(value)

    def Dequeue(self):
        return self.items.pop(0)

    def Size(self):
        return len(self.items)

    def Value(self):
       return self.items
shelf = input('Enter Input : ').split('/')
defaultbook = shelf[0].split()
rearr = shelf[1].split(',')
print('default book :',end=' ')
for i in defaultbook:
    print(i,end=', ')
print()
print('re-arrange : ',end='')
for i in rearr:
    print(i,end=', ')
print()
for i in range(len(rearr)):
    temp=rearr[i].split()
    print('temp : '+str(temp))
    if temp[0] == 'E':


