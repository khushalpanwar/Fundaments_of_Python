def sum_of_first_n_positive_integers(n):
    if n <= 0:
        return "Please enter a positive integer."
    else:
        return sum(range(1, n+1))

# Taking input from user
n = int(input("Enter a positive integer (n): "))

result = sum_of_first_n_positive_integers(n)
print("Sum of the first", n, "positive integers:", result)
