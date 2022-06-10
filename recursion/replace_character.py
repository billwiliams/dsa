# replace a characeter recursively


def replace_char(string,current_char,replacing_char,index):
    if index==len(string):
        return string

    if string[index]==current_char:
        string[index]=replacing_char
    return replace_char(string,current_char,replacing_char,index+1)

print(replace_char(['a','b','c','a'],'a','z',0))