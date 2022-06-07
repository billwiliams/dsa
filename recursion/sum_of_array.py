# recursively sum up elements in an array

def sum_of_array(array,array_size):

    # Base case
    if array_size==1:
        return array[0]
    
    # recursive case
    small_array_sum=sum_of_array(array[1:],array_size-1)

    #calculation
    return array[0] +small_array_sum

print(sum_of_array([1,2,3],3))
print(sum_of_array([1],1))
print(sum_of_array([10,20,30,40,1,2,3],7))