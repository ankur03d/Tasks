from functools import total_ordering  

print("--- Welcome to Result Dashboard ---\n")


name = input("Enter your name: ")
seat_no = input("Enter your seat number: ")


eng = int(input("Enter marks in English: "))
maths = int(input("Enter marks in Maths: "))
history = int(input("Enter marks in History: "))
python = int(input("Enter marks in Python: "))
da = int(input("Enter marks in Data Analytics: "))


total = eng + maths + history + python + da
percentage = total / 5


print(f"\nHello {name},")
print(f"Your seat number: {seat_no}")
print(f"Your total marks is {total}")
print(f"Your percentage is {percentage:.2f}%")
