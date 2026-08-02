def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n): # Generate Fibonacci series up to n terms
        series.append(a) # Add the current value of a to the series
        a, b = b, a + b
    return series

num_terms = int(input("Enter the number of terms for Fibonacci series: "))
if num_terms <= 0:
    print("Please enter a positive integer.", num_terms)
else:
    result = fibonacci(num_terms)
    print(f"The Fibonacci series up to {num_terms} terms is: {result}")



