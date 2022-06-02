#Recursively Print numbers from 1 to n

def print_numbers(n):
    #base case 
    print(n)
    if n==1:
        return
    
    return print_numbers(n-1)

print_numbers(n=10)

def print_numbers_recursively(n):
    if n==1:
        return n
    return n , print_numbers_recursively(n-1)
print(print_numbers_recursively(10))