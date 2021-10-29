jewels = input()
stones = input()

count = 0
for i in stones:
    if i in jewels:
        count += 1

print(count)