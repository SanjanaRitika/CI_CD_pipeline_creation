def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
