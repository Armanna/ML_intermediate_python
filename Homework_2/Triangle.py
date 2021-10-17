def triangle(a, b, c):
    aa = a * a
    bb = b * b
    cc = c * c

    if a + b <= c or a + c <= b or b + c <= a:
        print("No triangle")
    elif aa + bb == cc or aa + cc == bb or bb + cc == aa:
        print("Right triangle")
    elif aa + bb <= cc or aa + cc <= bb or bb + cc <= aa:
        print("Obtuse")
    else:
        print("Acute triangle")

a = int(input())
b = int(input())
c = int(input())

triangle(a, b, c)

