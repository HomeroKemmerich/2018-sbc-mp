"""
time@2025-04-18: 15:56
"""

n = input()

def is_prime(number: int) -> bool:   
    for i in range(2, int(number / 2)):
        if number % i == 0:
            return False
    return True

def is_even(number: int) -> bool:
    return number % 2 == 0

if is_prime(n):
    print(1)
elif is_even(n):
    print(2)
else:
    print(0)

