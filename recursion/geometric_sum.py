#recursively implementation of geometric sum

def geometric_sum(k):

    # Base Case
    if k==0:
        return 1

    #Recursive case
    ans=geometric_sum(k-1)

    #Calculation
    return 1.0/(2**k) +ans


print(geometric_sum(0))
print(geometric_sum(3))
print(geometric_sum(10))
