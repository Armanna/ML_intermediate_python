x = int(input())

root = int(x ** 0.5)
count = 0

while root > 0:
    if x % root == 0:
        count += 1
    root -= 1


if x == 1:
    print(1)
elif x % x**0.5 == 0:
    print((count - 1) * 2 + 1)
else:
    print(count * 2)