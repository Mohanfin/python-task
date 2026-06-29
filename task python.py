#1.find the last dig no
"""num=int(input("enter the number"))
last_digit =num%10
print("last digit is:",last_digit)"""
#2.remove last digit the code
"""num = int(input("Enter a number: "))
remove_last = num // 10
print("After removing last digit:", remove_last)
num = int(input("Enter a number: "))"""
#3find last two digit
"""num = int(input("Enter a number: "))
last_two = num % 100
print("Last two digits:", last_two)"""
#4.square the middle digit of a five digit num
"""num = int(input("Enter a five digit number: "))
middle_digit = (num // 100) % 10
square = middle_digit ** 2
print("Middle digit:", middle_digit)
print("Square of", middle_digit, "is:", square)"""
#5.bmi calculater
"""weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))
bmi = weight / ((height / 100) ** 2)
print("BMI is:", bmi)"""
#6.expand the number
"""num = input("Enter a number: ")
length = len(num)
for i in range(length):
    digit = int(num[i])
    if digit != 0:
 value = digit * (10 ** (length - i - 1))
        print(value, end=" ")
if i != length - 1:
            print("+", end=" ")"""
#7.volume of cylinder formula
"""a=float(input("Enter a number: "))
b=float(input("Enter radius: "))
c=b**2
d=float(input("Enter the height: "))
e=a*c*d
print(e)"""
#8.lume of cuboid
""" float(input("Enter the length: "))
b= float(input("Enter the breath: "))
c=float(input("Enter the height: "))
d=float(input("Enter the weight: "))
e=(a*b*c*d)
print(e)"""
#convert centimeter to meter
"""loat(input("Enter a number: "))
b=a**3
print(b)"""
10.ap two number using xor opertor
a=6
b=7
a=a^b
b=a^b
print("after swapping")
print(a=",a)
print(b=",b)
