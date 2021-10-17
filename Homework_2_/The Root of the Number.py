def sum_of_digits(n):
    sum = 0

    while n > 0:
        sum += n % 10
        n //= 10

    return sum


def root(n):
    print(n)
    while n > 0 and not n < 10:
        print(sum_of_digits(n))
        n = sum_of_digits(n)


n = int(input())

root(n)
