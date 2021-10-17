n = int(input())

product = 1

while n > 0:
    if n % 10 > 0:
        product *= n % 10
    n //= 10

print(product)
