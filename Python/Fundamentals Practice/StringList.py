#Find and Replace

str = "it's thanksgiving day It's my birthday,too!"

print str
print str.find("thanksgiving")
str = str.replace("birthday", "birthmonth")
print str

#Min/Max

x = [19,2,54,-2,7,12,98,32,10,-3,6]

print min(x)
print max(x)

#First/Last

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]

#New List

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first_list = x[0:len(x)/2]
print first_list
second_list = x[len(x)/2:]
print second_list
second_list.insert(0,first_list)
print second_list