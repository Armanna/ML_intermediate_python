def beautifulBinaryString(b):
    count = 0
    i = 0
    while i < len(b) - 1:
        if b[i:i+3] == "010":
            count += 1
            i += 3
            continue
        i += 1
    print(count)


n = int(input())

b = input()

result = beautifulBinaryString(b)




