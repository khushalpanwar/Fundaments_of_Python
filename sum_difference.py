#  QUESTION : Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.


def check_values(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5

# Example usage:
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if check_values(num1, num2):
    print("True")
else:
    print("False")
