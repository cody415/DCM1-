def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter the number of terms: "))
fib_series = fibonacci(n)

print("Fibonacci series up to", n, "terms:")
for num in fib_series:
    print(num, end=" ")
