# Count the numbers of zeroes recursively

def zeroes(n):
    
    #Base Case
    if n <=0:
        return 0
    divisibe_by_ten=False
    if n%10==0:
        divisibe_by_ten=True
    return int(divisibe_by_ten) +zeroes(n//10)


print(zeroes(10))
print(zeroes(10001))
print(zeroes(12342343401))
print(zeroes(100303400001))
print(zeroes(10))