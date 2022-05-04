def alphabet(alpha: str) -> int:
    value: str
    if ('a' in alpha) or ('b' in alpha) or ('c' in alpha):
        value = "2"
    elif ('d' in alpha) or ('e' in alpha) or ('f' in alpha):
        value = "3"
    elif ('g' in alpha) or ('h' in alpha) or ('i' in alpha):
        value = "4"
    elif ('j' in alpha) or ('k' in alpha) or ('l' in alpha):
        value = "5"
    elif ('m' in alpha) or ('n' in alpha) or ('o' in alpha):
        value = "6"
    elif ('p' in alpha) or ('q' in alpha) or ('r' in alpha) or ('s' in alpha):
        value = "7"
    elif ('t' in alpha) or ('u' in alpha) or ('v' in alpha):
        value = "8"
    elif ('w' in alpha) or ('x' in alpha) or ('y' in alpha) or ('z' in alpha):
        value = "9"

    return value


def phoneWord2Num(word: str) -> None:
    word = word.lower()
    if len(word) == 7:
        value = alphabet(word[0]), alphabet(word[1]), alphabet(word[2]), alphabet(
            word[3]), alphabet(word[4]), alphabet(word[5]), alphabet(word[6])
        value = int("".join(value))
        return value
    else:
        return None

print(phoneWord2Num("PrOGrAM"))