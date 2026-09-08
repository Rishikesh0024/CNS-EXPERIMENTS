import random
import time
import math

# Trial Division
def trial_division(n):
    if n < 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


# Fermat Primality Test
def fermat_test(n, k=5):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)

        if math.gcd(a, n) != 1:
            return False

        if pow(a, n - 1, n) != 1:
            return False

    return True


# Main Program
n = int(input("Enter a number: "))


# Trial Division
start = time.perf_counter()
result1 = trial_division(n)
time1 = time.perf_counter() - start


# Fermat Test
start = time.perf_counter()
result2 = fermat_test(n)
time2 = time.perf_counter() - start


# Display Results
print("\nResults:")

print(
    "Trial Division:",
    "Prime" if result1 else "Composite"
)

print(
    "Time:",
    format(time1, ".8f"),
    "seconds"
)

print(
    "\nFermat Test:",
    "Probably Prime" if result2 else "Composite"
)

print(
    "Time:",
    format(time2, ".8f"),
    "seconds"
)