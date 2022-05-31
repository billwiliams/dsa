# recursive power function

def power(n,pow):
    if pow==0:
        return 1
    return n*power(n,pow-1)

print(power(2,0))
print(power(2,2))
print(power(2,5))
print(power(10,10))