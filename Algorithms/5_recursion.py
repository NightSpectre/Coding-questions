# Recursion - The function which keeps on calling itself until a specific condition is met

# Find factorial of a number by recursion

def factorial(n):
    if n==0:
        return 1
    return n*(factorial(n-1))

n=5
res=factorial(n)
print(res)
