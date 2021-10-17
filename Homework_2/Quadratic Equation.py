a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Non-quadratic equation")
            print("Infinite solutions")
        else:
            print("Non-quadratic equation")
            print("No Solutions")
    else:
        print("Non-quadratic equation")
        print("One Solution:", -c/b)
else:
    D = b**2 - 4 * a * c
    x_1 = (-b - D**0.5) / (2 * a)
    x_2 = (-b + D**0.5) / (2 * a)
    print("Quadratic equation")
    print("Discriminant:", D)
    if D < 0:
        print("No Solutions")
    elif D == 0:
        print("One Solution:", x_1)
    else:
        print("Two Solutions:", x_1, x_2)