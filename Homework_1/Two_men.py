first = int(input())
second = int(input())

number_of_cans = first + second - 1


first_missed = number_of_cans - first
second_missed = number_of_cans - second

print(first_missed)
print(second_missed)