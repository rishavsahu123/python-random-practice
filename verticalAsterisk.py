def getDataAsterisk(data=[]):
    data_sort = sorted(data)
    max_num = data_sort[len(data_sort)-1]
    for i in range(max_num, 0, -1):
        for j in range(len(data)):
            if(data[j]>=i):
                print('*', end='')
            else:
                print(' ', end='')
        print('\n')

list = [1,4,5,3,7,3]
getDataAsterisk(list)