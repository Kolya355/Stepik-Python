print("    ------------------------------------Choose a mode------------------------------------")
print("1 - Simple Operations(+,-,/,*). 2 - Discriminant. 3 - Pythagorean theorem. 4 - Area calculation")
choose = int(input())

if choose == 1:
    print("Choose operation")
    print("1 - '+'. 2 - '-'. 3 - '*'. 4 - '/'")
    operation_choose = int(input())
    if operation_choose == 1:
        a = float(input("Print first addend: "))
        b = float(input("Print second addend: "))
        print("Result =", a + b)
    elif operation_choose == 2:
        a = float(input("Print minuend: "))
        b = float(input("Print subtrahend: "))
        print("Result =", a - b)
    elif operation_choose == 3:
        a = float(input("Print multiplicand: "))
        b = float(input("Print multiplier: "))
        print("Result =", a * b)
    elif operation_choose == 4:
        a = float(input("Print dividend: "))
        b = float(input("Print divisor: "))
        if b == 0:
            print("Error: Division by Zero")
        else:
            print("Result =", a / b)
    else:
        print("Error: Not valid operation")
elif choose == 2:
    b = float(input("Print variable b: "))
    a = float(input("Print variable a: "))
    c = float(input("Print variable c: "))
    if a == 0:
        print("'a' can't be 0")
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b+D**0.5)/(2*a)
        x2 = (-b-D**0.5)/(2*a)
        print("First root:", x1)
        print("Second root:", x2)
    elif D == 0:
        print("Root:", -b/(2*a))
    elif D < 0:
        print("No real roots")
elif choose == 3:
    a = float(input("Print first cathetus: "))
    b = float(input("Print second cathetus: "))
    c = (a**2+b**2)**0.5
    print("Hypotenuse:", c)
elif choose == 4:
    print("Choose operation")
    print("1 - Parallelogram. 2 - Triangle. 3 - Trapezium. 4 - Rectangle. 5 - Square. 6 - Rhombus.")
    operation_choose = int(input())
    if operation_choose == 1:
        a = float(input("Print side: "))
        b = float(input("Print height: "))
        print("Area:", a*b)
    elif operation_choose == 2:
        a = float(input("Print side: "))
        h = float(input("Print height: "))
        print("Area: ", 0.5*a*h)
    elif operation_choose == 3:
        a = float(input("Print first base: "))
        b = float(input("Print second base: "))
        h = float(input("Print height: "))
        print("Area:", (a+b)/2*h)
    elif operation_choose == 4:
        a = float(input("Print side(horizontal): "))
        b = float(input("Print side(verticcal): "))
        print("Area:", a*b)
    elif operation_choose == 5:
        print("Choose method")
        print("1 - With side. 2 - With diagonal")
        ec = int(input())
        if ec == 1:
            a = float(input("Print side: "))
            print("Area: ", a**2)
        elif ec == 2:
            d = float(input("Print diagonal: "))
            print("Area: ", 0.5*d**2)
    elif operation_choose == 6:
        d1 = float(input("Print first diagonal: "))
        d2 = float(input("Print second diagonal: "))
        print("Area:", 0.5*d1*d2)
    else:
        print("Error: Not valid operation")
else:
    print("Error: Not valid operation")
