# recursively remove an element from an array

def remove_element(array,element,index=0):
    if len(array)==index:
        return array
    else:
        if array[index]==element:
            del array[index]
            return remove_element(array,element,index)
        return remove_element(array,element,index+1)

print(remove_element([0,1,2,0,3,0],0,0))
print(remove_element([0,1,2,0,3,0],5))