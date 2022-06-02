#Recursively Print numbers from 1 to n

def print_numbers_ascending(n):
    #base case 
    
    if n==1:
        print(n)
        return 
    
    print_numbers_ascending(n-1)
    print(n)



print_numbers_ascending(n=10)

def print_numbers_descending(n):
    if n==1:
        print(n)
        return
    print(n)
    print_numbers_descending(n-1)

print_numbers_descending(10)
