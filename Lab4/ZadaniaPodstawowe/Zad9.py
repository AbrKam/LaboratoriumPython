def fib(m):
    if m == 1 or m == 0:
        return 1
    else:
        return fib(m - 1) + fib(m - 2)

print(fib(8))