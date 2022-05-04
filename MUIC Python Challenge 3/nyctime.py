def nycHour(bkkHour: int) -> str:
    bkkHour = bkkHour % 24
    if bkkHour >= 0 and bkkHour < 11:
        nyctime = 12 + (bkkHour - 11)
        return "{}pm".format(nyctime)
    elif bkkHour >= 12 and bkkHour < 23:
        nyctime = bkkHour - 11
        return "{}am".format(nyctime)
    else:
        if bkkHour == 23:
            return "12pm"
        else:
            return "12am"

print(nycHour(23))
