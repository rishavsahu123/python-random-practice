from array import *
"""
Typecode		Value
	b			Represents signed integer of size 1 byte/td>
	B			Represents unsigned integer of size 1 byte
	c			Represents character of size 1 byte
	i			Represents signed integer of size 2 bytes
	I			Represents unsigned integer of size 2 bytes
	f			Represents floating point of size 4 bytes
	d			Represents floating point of size 8 bytes
arrayName = array(typecode, [Initializers])

Following are the basic operations supported by an array.
Traverse- print all the array elements one by one.
Insertion - Adds an element at the given index.
Deletion- Deletes an element at the given index.
Search - Searches an element using the given index or by the value.
Update- Updates an element at the given index.

arrayObj = array('I',[10,20,30,40,50])
"""

class Array(object):
	def __init__(self):
		self.arrayObj = array('i',[10,20,30,40,50])
		print("Your dummy array is:\n")
		for i in self.arrayObj:
			print(i);
		print("Enter number for action perform:\n \
				1 for traverse \n \
				2 for insertion \n \
				3 for deletion \n \
				4 for search \n \
				5 for update")
		# use input() for python3
		input = raw_input("Enter above number to perform action:")
		if(input == "1"):
			for i in self.arrayObj:
				print(i);
		elif(input == "2"):
			eventValue = int(raw_input("Enter value for insert"))
			insertPosition = int(raw_input("Enter insert position"))
			self.insert(eventValue, insertPosition);
		elif(input == "3"):
			eventValue = int(raw_input("Enter value for delete"))
			self.delete(eventValue);
		elif(input == "4"):
			eventValue = raw_input("Enter value for search")
			insert(eventValue);
		elif(input == "5"):
			targetValue = raw_input("Enter which value you want to update")
			eventValue = raw_input("Enter value for update")
			insert(eventValue);

	def insert(self, val, insertPosition):
		count = 0
		insertFlag = False
		iterationArray = []
		import pdb;pdb.set_trace()
		while(len(self.arrayObj)>=count):
			if(insertPosition == count and not insertFlag):
				iterationArray.append(val);
				insertFlag = True;
			elif(insertFlag):
				iterationArray.append(self.arrayObj[count-1])
			else:
				iterationArray.append(self.arrayObj[count])
			count+=1

	def delete(self, val):
		iterationArray = []
		


Array();
