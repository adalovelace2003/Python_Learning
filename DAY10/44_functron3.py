# n! = 1 * 2 * 3 * 4 ... *n


n = 4

def factorial_iter(n):
    
    product = 1
    for i in range(n):
        product = product * (i+1)
        
    return product

print(factorial_iter(5))