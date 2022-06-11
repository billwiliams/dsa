# recursively print all subsequencies of a string

def print_subsequence(in_str,out_str):
    if len(in_str)==0:
        print(out_str)
        return
    print_subsequence(in_str[1:],out_str)
    print_subsequence(in_str[1:],in_str+out_str)


print_subsequence("abc","")