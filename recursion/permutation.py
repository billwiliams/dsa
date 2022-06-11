# recursively print all permutations of a string

def permutations(string,index):
    if len(string)==index:
        print(string)
        return
    else:

        for i in range(index,len(string)):
            string[i],string[index]=string[index],string[i]
            permutations(string,index+1)
            string[i],string[index]=string[index],string[i]

permutations(['a','b','c'],0)


