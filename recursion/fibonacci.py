# recursive Fibonacci function

def fibonacci(n):
    #base case
    if n==2 or n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))