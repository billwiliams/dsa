# Count number of digits in a  positive or negative number number

def number_of_digits(n):
    if n<0:
        n= abs(n)
    if n/10<1:
        return 1
    return 1 + number_of_digits(n//10)


print(number_of_digits(0))
print(number_of_digits(110))
print(number_of_digits(305098843))
print(number_of_digits(-305098843))


    