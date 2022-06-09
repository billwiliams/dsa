# recursively find the length of a string or array

def length(array):
    if len(array)==0:
        return 0
    return 1 +length(array[1:])


print(length([0,1,2,3,4]))