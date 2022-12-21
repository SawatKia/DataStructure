def group(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))
print("*** Converting hh.mm.ss to seconds ***")
hh, mm, ss=input("Enter hh mm ss : ").split()
h=int(hh)
m=int(mm)
s=int(ss)
second=(s+(m*60)+(h*60*60))
if h<10:
    hh="0"+hh
if m<10:
    mm="0"+mm
if s<10:
    ss="0"+ss

if m>=60 or m<0 :
    print("mm("+str(m)+") is invalid!")
elif s<0 or s>60 :
    print("ss("+str(s)+") is invalid!")
elif h<0 :
    print("hh("+str(h)+") is invalid!")
else :
    print(hh+":"+mm+":"+ss+" = "+str(group(second))+" seconds")