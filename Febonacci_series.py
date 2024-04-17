def fibonacci_range(start, end):
    fib_series = []
    a, b = 0, 1
    while a < end:
        if a >= start:
            fib_series.append(a)
        a, b = b, a + b
    return fib_series

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

fib_series = fibonacci_range(start, end)
print("Fibonacci series within the range {} to {}: {}".format(start, end, fib_series))
