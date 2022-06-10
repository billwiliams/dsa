# recursively convert string to integer

def str_to_int(string):
    if len(string)==0:
        return 0
    
    return str_to_int(string[:-1])*10 + int(string[-1])


print(str_to_int("123"))