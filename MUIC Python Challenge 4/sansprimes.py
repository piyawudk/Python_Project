def is_prime(n: int) -> bool:
    while n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

def sans_primes(numbers: list) -> list:
    numbers.append(0)
    z = []
    for i in range(len(numbers)-1):
        if not is_prime(numbers[i]):
            if not is_prime(numbers[i-1]):
                z.append(numbers[i])
    return z

print(sans_primes([1, 0, 3, 0, -2, 5, 7, 1, 42, 9]))
