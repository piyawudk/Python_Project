def sumOfDigitsSquared(n: int) -> int:
    b = 0
    x = list(str(n))
    for i in range(len(x)):
        z = int(x[i])
        b+=z**2
    return b
        
def isHappy(n: int) -> bool:
    if n > 0:
        while (n != 4):
            n = sumOfDigitsSquared(n)
            if n == 1:
                return True
        return False
    else:
        return None

def kThHappy(k: int) -> int:
    z = []
    for i in range(1000):
        if isHappy(i) is True:
            z.append(i)
    return z[k-1]

print(isHappy(989))