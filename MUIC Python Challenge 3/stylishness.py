def got_table(you: int, date: int) -> str:
    you = you % 10
    date = date % 10
    if you >= 8 or date >= 8:
        return "yes"
    elif you <= 2 or date <= 2:
        return "no"
    else:
        return "maybe"

print(got_table(7, 8))
