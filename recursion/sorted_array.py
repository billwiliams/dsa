# recursively check if an array is sorted

def is_sorted_array(array,length_of_array):

    if length_of_array==1:
        return True
    
    if (array[0]<array[1]):
        return is_sorted_array(array[1:],length_of_array-1)
    else:
        return False


print(is_sorted_array([0],1))
print(is_sorted_array([1,2,3,4,5],5))
print(is_sorted_array([1,2,3,5,4],5))
print(is_sorted_array([1,2,3,5,19],5))