s = input()
ss = input()

print(s)

n = int(s[0])
k = int(s[2])

k = k % n

l = list(map(lambda x: int(x), ss.split()))

new_l = []

for i in range(n - k, n):
    new_l.append(l[i])
for i in range(n - k):
    new_l.append(l[i])

print(new_l)