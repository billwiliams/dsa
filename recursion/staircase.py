# recursively count number of jumps possible given jump can be 1,2 or 3

def staircase(n):
    #Base Case
    if n<0:
        return 0
    if n==0:
        return 1
    
    # recursive Case
    return staircase(n-1)+staircase(n-2)+staircase(n-3)


print(staircase(1))
print(staircase(3))
print(staircase(5))