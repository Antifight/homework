#1
user_number = int(input("Enter a number: "))
if user_number % 3 == 0 and user_number % 5 == 0:
    print("ham")
elif user_number % 3 == 0:
    print("foo")
elif user_number % 5 == 0:
    print("bar")
else:
    print("number cannot be divisible by 3 and 5")

#2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 > num2:
    print("First number is greater than second number")
elif num1 < num2:
    print("First number is less than second number")
else:
    print("Your numbers are equal")

#3
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
list1 = [num1, num2, num3]
list1.sort()
print(list1)

#4
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#5

for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        print("BOOM")
    else:
        print(i)