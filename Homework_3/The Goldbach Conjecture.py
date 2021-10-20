def prime(a):
    root_a = int(a**0.5)
    while root_a > 1:
        if a % root_a == 0:
            return False
        root_a -= 1
    return True

def sum_of_primes(n):
    half = n // 2
    for i in range(2, half + 1):
        if prime(i) and prime(n - i):
            print(i, n - i)
            return

n = int(input())

sum_of_primes(n)


