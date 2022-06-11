# recursively count the occurence of an element in an array

def count_occurence(array,element,index=0):

    if len(array)==index:
        return 0

    else:
        if array[index]==element:
            return 1 +count_occurence(array,element,index+1)
    return count_occurence(array,element,index+1)


print(count_occurence([0,1,0,0,1,2,0],0,0))
print(count_occurence([0,1,0,0,1,2,0],5,0))