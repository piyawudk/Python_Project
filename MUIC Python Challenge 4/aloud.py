def readAloud(lst: list) -> list:
    z = []
    key = 1
    lst.append(0)
    for m in range(len(lst)-1):

        if lst[m+1] == lst[m]:
            key+=1
        else:
            z.append(key)
            z.append(lst[m])
            key = 1
    return z

print(readAloud([3,3,1,1,3,1,1]))