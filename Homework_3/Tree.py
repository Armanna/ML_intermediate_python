n = int(input())

j = 1
for i in range(1, n + 1):
    if j > n:
        break
    print(' ' * ((n - j) // 2), '*' * j, ' ' * ((n - j) // 2), sep='')
    j += 2
