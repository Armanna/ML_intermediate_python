s = input()

str = s[:s.find(" ")]
n = int(s[s.find(" ") + 1:])


if n >= 0:
    print(str * n)
else:
    n *=(-1)
    substr_length = len(str) // n
    if str[:substr_length] * n == str:
        print(str[:substr_length])
    else:
        print("undefined")


