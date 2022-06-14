# return the number of steps in tower of hanoi

def toh_steps(n):
    if n==0:
        return 0
    
    return toh_steps(n-1)+toh_steps(n-1)+1


print(toh_steps(3))
print(toh_steps(5))