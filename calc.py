from math import hypot, pi

def simple_operation():
        print("<--------Choose operation-------->")
        print("1 - '+'. 2 - '-'. 3 - '*'. 4 - '/'")
        operation_choose = int(input())
        if operation_choose == 1:
            a = float(input("Print first addend: "))
            b = float(input("Print second addend: "))
            return f"Result = {a + b}"
        elif operation_choose == 2:
            a = float(input("Print minuend: "))
            b = float(input("Print subtrahend: "))
            return f"Result = {a - b}"
        elif operation_choose == 3:
            a = float(input("Print multiplicand: "))
            b = float(input("Print multiplier: "))
            return f"Result = {a * b}"
        elif operation_choose == 4:
            a = float(input("Print dividend: "))
            b = float(input("Print divisor: "))
            if b == 0:
                return "Error: Division by Zero"
            else:
                return f"Result = {a / b}"
        else:
            return "Error: Not valid operation"
def discriminant():
        a = float(input("Print variable a: "))
        if a == 0:
            return "'a' can't be 0"
        b = float(input("Print variable b: "))
        c = float(input("Print variable c: "))
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + D**0.5) / (2*a)
            x2 = (-b - D**0.5) / (2*a)
            return f"First root: {x1}\nSecond root: {x2}" 
        elif D == 0:
            root = -b / (2*a)
            return f"Root: {root}"
        else:
            return "No real roots"
def Area():
        print("<", "Choose operation", ">", sep="-"*40)
        print("1 - Parallelogram. 2 - Triangle. 3 - Trapezium. 4 - Rectangle. 5 - Square. 6 - Rhombus. 7 - Circle.")  ##Figure choose
        operation_choose = int(input())
        if operation_choose == 1:
            a = float(input("Print side: "))
            b = float(input("Print height: "))
            return f"Area: {a*b}"
        elif operation_choose == 2:
            a = float(input("Print side: "))
            h = float(input("Print height: "))
            return f"Area: {0.5*a*h}"
        elif operation_choose == 3:
            a = float(input("Print first base: "))
            b = float(input("Print second base: "))
            h = float(input("Print height: "))
            return f"Area: {(a+b)/2*h}"
        elif operation_choose == 4:
            a = float(input("Print side(horizontal): "))
            b = float(input("Print side(vertical): "))
            return f"Area: {a*b}"
        elif operation_choose == 5:
            print("Choose method")
            print("1 - With side. 2 - With diagonal")
            method = int(input())
            if method == 1:
                a = float(input("Print side: "))
                return f"Area: {a**2}"
            elif method == 2:
                d = float(input("Print diagonal: "))
                return f"Area: {0.5*d**2}"
            else:
                return "Error: Not valid operation"
        elif operation_choose == 6:
            d1 = float(input("Print first diagonal: "))
            d2 = float(input("Print second diagonal: "))
            return f"Area: {0.5*d1*d2}"
        elif operation_choose == 7:
            r = float(input("Input radius: "))
            return f"Area: {pi*r**2}"
        else:
            return "Error: Not valid operation"

while True:
    print("<", "Choose a mode", ">", sep = "-"*40)
    print("1 - Simple Operations(+,-,/,*). 2 - Discriminant. 3 - Pythagorean theorem. 4 - Area calculation. 5 - Linear equation. 0 - Exit.")  ##Mode choose
    choose = int(input())

    if choose == 1:
        result = simple_operation()
        print(result)
    elif choose == 2:
        root = discriminant()
        print(root)
    elif choose == 3:
        a = float(input("Print first cathetus: "))
        b = float(input("Print second cathetus: "))
        print(f"Hypotenuse: {hypot(a, b)}")
    elif choose == 4:
        area = Area()
        print(area)
    elif choose == 5:
        a = float(input("Input variable a: "))
        b = float(input("Input variable b: "))
        if a == 0:
            print("Error: variable a can't be 0")
        else:
            print(f"Root: {-b/a}")
    elif choose == 0:
        print("Goodbye!")
        break
    else:
        print("Error: Not valid operation")