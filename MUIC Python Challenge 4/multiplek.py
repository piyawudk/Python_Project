def allMultiplesOfK(k: int, lst: list) -> bool:
    status = True
    if lst:
        for i in lst:
            if i%k != 0 :
                status = False
        return status
    else:
        return True

print(allMultiplesOfK(3, [81,3,24]))