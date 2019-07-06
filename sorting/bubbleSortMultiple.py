list = [23,446,45,6,676,732,24534,23]
list1 = [23,446,45,6,676,732,24534,23]
for i in range(len(list)):
    for j in range(len(list)-1-i):
        if(list[j]>list[j+1]):
            list[j],list[j+1] = list[j+1],list[j]

for i in range(len(list1)-1,0,-1):
    for j in range(i):
        if(list1[j]>list1[j+1]):
            list1[j],list1[j+1] = list1[j+1],list1[j]

print(list)
print(list1)