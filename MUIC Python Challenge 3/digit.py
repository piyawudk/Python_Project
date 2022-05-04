# support up to base 36 using rapidtable's algorithm
a = []
ans = ''
def kthDigit(x: int, b: int, k: int) -> int:
    # quotient
    z = x//b
    # remainder
    y = x % b
    if z == 0:
        z = x//b
        y = x%b
        a.append(y)
        a.reverse()
        if k > (len(a)-1):
            return 0
        else:
            z = a[-1-k]
            return z
    a.append(y)
    return kthDigit(z, b, k)

print(kthDigit(987, 16, 0))
