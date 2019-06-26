pos = -1
def linearSearch(list, val):
    for i in list:
        global pos
        pos += 1
        if(i == val):
            return ('Found data at %s position!'%(pos+1))
    return ('data not found!!')

list = [12,34,45,56,78,4321,12,3]
print(linearSearch(list,78))