from collections import Counter
class funString():

    def __init__(self,string = ""):

        self.string=string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        return self.string.swapcase()


    def reverse(self):
        str = ""
        for i in self.string:
            str = i + str
        return str


    def deleteSame(self):
        pass
        #find duplicate
        WC = Counter(self.string)
        str=''
        strlist=[]
        strlist[:0]=self.string
        # Finding no. of  occurrence of a character
        # and get the index of it.
        duplicate = []
        for letter, count in WC.items():
            if (count > 1):
                duplicate.append(letter)
        #delete duplicate
        for i in range(0,len(duplicate)):
            j=i+1
            while j<len(strlist)-1:
                check = duplicate[i]
                tocheck = strlist[j]
                if duplicate[i] == strlist[j]:
                    strlist.pop(j)
                else:
                    j += 1
        text=''
        for i in strlist:
            text = text+i
        return text



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :
    print(res.size())

elif str2 == "2":
    print(res.changeSize())

elif str2 == "3" :
    print(res.reverse())

elif str2 == "4" :
    print(res.deleteSame())