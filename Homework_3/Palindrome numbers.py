def palindrome(num):
    num = str(num)
    l = len(num)
    l_half = l // 2
    for i in range(l_half):
        if num[i] != num[-1 - i]:
            return False
    return True


a = int(input())
b = int(input())

for i in range(a, b + 1):
    if palindrome(i):
        print(i, end=" ")

