print("Simple Calculator")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter 1, 2, 3, or 4: ")

if operation == "1":
    print("Result:", num1 + num2)
elif operation == "2":
    print("Result:", num1 - num2)
elif operation == "3":
    print("Result:", num1 * num2)
elif operation == "4":
    if num2 == 0:
        print("Error! Cannot divide by zero.")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid choice!")
