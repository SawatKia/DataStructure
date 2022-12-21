print("*** Reading E-Book ***")
txt = input("Text , Highlight : ")
txt_split=txt.split(",")
#txt_split[0]=text
#txt_split[1]=char
lst =[]
for pos,char in enumerate(txt_split[0]):
    if(char == txt_split[1]):
        lst.append(pos)
#print(lst)
char = list(txt_split[0])
pos=0
for pos in lst :
    char[pos] = "["+char[pos]+"]"
    #print(char[pos])
for pos in char:
    print(pos,end ='')

