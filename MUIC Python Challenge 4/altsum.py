def altSum(lst: list) -> int:
    y,z = 0,0
    j = []
    if lst:
        # get even number list
        for i in range(0,len(lst),2):
            j.append(lst[i])
        # get and add odd number list
        for i in range(1,len(lst),2):
            z = lst[i]+z

        y = -(sum(j[1:]))
        y = j[0] + y + z
        return y
    else:
        return 0

print(altSum([31,4,28,5,71]))
