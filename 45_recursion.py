def factorail_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * factorail_recursive(n-1))

print(factorail_recursive(5))

