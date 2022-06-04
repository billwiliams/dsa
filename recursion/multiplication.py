# recursively multiply two numbers

def multiply(m,n):
    #Base Case
    if n==0:
        return 0
    return m + multiply(m,n-1)

print(multiply(10,2))
print(multiply(10,0))
print(multiply(30,40))
