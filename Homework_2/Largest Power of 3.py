def power_of_3(n):
    if n == 1:
        return 0
    count = 0
    while n > 1:
        if n % 3 != 0:
            return -1
        count += 1
        n //= 3
    return count




def largest_power_of_3(n):
    max_power = 0
    max_number = 1
    for i in range(3, n + 1):
        if power_of_3(i) > max_power:
            max_power = power_of_3(n)
            max_number = i
    return max_number


n = int(input())

print(largest_power_of_3(n))

