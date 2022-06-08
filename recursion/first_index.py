# recursively check the first index of an element in an array

def first_index(array,array_size, element,index):

    if index==array_size:
        return False
    else:
        if array[index]==element:
            return index
        else:
            return first_index(array,array_size,element,index+1)


print(first_index([0,1,2,3,4],5,4,0))
print(first_index([0,1,2,3,4],5,7,0))