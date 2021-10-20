line = input()

l = list(map(lambda x: float(x),line.split()))

new_l = []


for i in range(len(l)):
    sum = 0
    for j in range(i, len(l)):
        sum += l[j]
    new_l.append(sum)


print(new_l)

