# Recursively get the indices of an element in an array

def element_positions(array,element,index,positions):

    # Base Case

    if index<0:
        return positions
    else:
        if array[index]==element:
            positions.append(index)
        return element_positions(array,element,index-1,positions)

print(element_positions([0,1,2,3,4,0,0],0,6,[]))
print(element_positions([0,1,2,3,4,0,0],13,6,[]))