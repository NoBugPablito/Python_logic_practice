# Create a function is_prime(n) that returns True if the number is a prime, or False if not.

def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2, n):
            if (n % i == 0):
                status = False
                break
    return status

n = int(input("Enter number "))
result = is_prime(n)
print(result)