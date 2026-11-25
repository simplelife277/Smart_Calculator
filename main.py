# DAY 1 -SMART CALCULATOR

print("===============CALCULATOR===============")

#Get User Details
name = input("Enter Your Name: ")

#Get two number from customer
num1 = int(input("Enter Your 1st Number: "))
num2 = int(input("Enter Your 2nd Number:"))

#Perform Calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

#Display the Result
print("\nHello", name)

print("Your addition is ",addition)
print("Your subraction is ",subtraction)
print("You multiplication is ",multiplication)
print("Your division is ",division)