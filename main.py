def factorial(n):
    print("Request function factorial with n = ", n)
    if n == 1:
        print("Base case, n = 1, return 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Return result for n = ", n, ": ", result)
        return result

print(factorial(5))

