# recursively check for the last index of an element in an array


def last_index(array,element,index):

    if index<0:
        return False
    
    else:
        if array[index]==element:
            return index
        else:

            return last_index(array,element,index-1)

print(last_index([0,1,2,3,0],0,4))

print(last_index([0,1,2,3],0,3))
print(last_index([0,1,2,3],13,3))