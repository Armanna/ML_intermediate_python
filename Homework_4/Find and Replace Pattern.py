def make_list(s):
    d = dict()
    num = -1
    for i in s:
        if i not in d:
            num += 1
            d[i] = num

    l = []
    for i in s:
        l.append(d[i])

    return l


words = input().split()
pattern = input()

l_p = make_list(pattern)

result = []

for i in words:
    if make_list(i) == l_p:
        result.append(i)

print(result)


