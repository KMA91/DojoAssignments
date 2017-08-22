myList = ["1"]
newlist = []
sum = 0.00

for i in myList:
    if isinstance(i, str):
        newlist.append(i)
    else:
        sum+=i
print newlist
print sum