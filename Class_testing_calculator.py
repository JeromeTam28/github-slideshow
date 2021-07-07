print("Enter a number")
num1 = int(input())
print("Enter another number")
num2 = int(input())

print("What would you like to with the calculator?")
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division ")

choice = int(input())

result = "no answer"
operate = "?"
if choice == 1:
    result = num1 + num2
    operate = "+"
elif choice == 2:
    result = num1 - num2
    operate = "-"
elif choice ==3:
    result = num1 * num2
    operate = "*"
elif choice ==4:
    result = num1 / num2
    operate = "/"
else:
    print("Error. Wrong input.")

print(str(num1) + operate + str(num2) + "=" + str(result))


