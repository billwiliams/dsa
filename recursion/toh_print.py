# print the steps of tower of hanoi

def toh(n,source,helper,destination):
    if n==0:
        return 0

    else:
        toh(n-1,source,destination,helper)
        print(" Move disk "+ str(n)+ " from " +source +" to "+destination )
        toh(n-1,helper,source,destination)

(toh(3,"A","B","C"))