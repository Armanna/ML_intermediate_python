num = int(input())

first = num // 100
second = num // 10 % 10
third = num % 10

sum_of_digits = first + second + third

print(sum_of_digits)