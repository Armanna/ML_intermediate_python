words = input().split()


row1 = set("QWERTYUIOPqwertyuiop")
row2 = set("ASDFGHJKLasdfghjkl")
row3 = set("ZXCVBNMzxcvbnm")


res = []


for word in words:
    exists = True
    if word[0] in row1:
        for i in word[1:]:
            if i not in row1:
                exists = False
    elif word[0] in row2:
        for i in word[1:]:
            if i not in row2:
                exists = False
    else:
        for i in word[1:]:
            if i not in row3:
                exists = False

    if exists:
        res.append(word)


print(res)






