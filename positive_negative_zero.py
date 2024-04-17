# Write a Python program to check if a number is positive, negative or zero.

number = int(input("Enter the number which you want to check : "))

if number <= 0:
    print("Given number is Negative.")
elif number >= 0 :
    print("Given number is positive.")
else:
    print("Given number is zero.")