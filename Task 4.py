# Triangle Type Checker

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("This is an Equilateral Triangle.")
    elif a == b or b == c or a == c:
        print("This is an Isosceles Triangle.")
    else:
        print("This is a Scalene Triangle.")
else:
    print("The sides cannot form a triangle. Invalid Triangle.")
