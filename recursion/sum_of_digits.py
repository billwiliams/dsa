# Sum of digits in a number

def sum_of_digits(n):
    
    #Base Case
    if n<1:
        return 0
    
    small_sum=n%10

    return small_sum +sum_of_digits(n//10)


print(sum_of_digits(10))
print(sum_of_digits(123))
print(sum_of_digits(0))
print(sum_of_digits(1010123))

