# To check that given number is odd or even or zero :


number = int(input("Enter the number you want to check : "))

if number%2 == 0 :
    print("Given number is Even.")
elif number == 0 :
    print("Given number is zero.")
else : 
    print("Given number is Odd.")