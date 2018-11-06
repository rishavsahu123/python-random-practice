#Suppose, I have a list [12,35,43,3,34]
list = [12,35,43,3,34]
def manualAppend(val):
	# count = 0;
	# newList = []
	# while(len(list)>=count):
	# 	if(len(list) == count):
	# 		newList[count] = val
	# 		break;
	# 	newList[count] = list[count]
	# 	count+=1
	# return newList;
	return list+[val]

returnObj = manualAppend(100)
print(returnObj)


