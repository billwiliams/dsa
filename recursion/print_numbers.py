#Recursively Print numbers from 1 to n

def print_numbers(n):
    #base case 
    print(n)
    if n==1:
        return
    
    return print_numbers(n-1)

print_numbers(n=10)