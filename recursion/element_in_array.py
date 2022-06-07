# recursively check if an element exists in an array

def is_element_present(array,length_of_array,element):

    #Base Case
    if length_of_array==1:
        #Base Case
        if array[0]==element:
            return True
        else:
            return False
    #recursive Case
    if array[0]==element:
        return True
    return is_element_present(array[1:],length_of_array-1,element)

print(is_element_present([1,2,3,4],4,4))
print(is_element_present([1,2,3,4],4,5))
        