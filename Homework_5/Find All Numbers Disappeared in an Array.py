arr = input().split()
nums = list(map(int, arr))

n = len(nums)

nums = set(nums)
res = []

for i in range(1, n + 1):
    if i not in nums:
        res.append(i)

print(res)