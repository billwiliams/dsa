# recursively print items in an array or string

def print_forward(array,index):
    if len(array)==index:
        return 
    print(array[index])
    print_forward(array,index+1)

print_forward([1,2,3,4,5,6],0)