import math


# ---------------------------------------------------------
# Part A: Euclid's Algorithm
# ---------------------------------------------------------
def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


# ---------------------------------------------------------
# Part B: Fermat's Little Theorem
# ---------------------------------------------------------
def fermat_little_theorem(a, p):
    if euclid_gcd(a, p) != 1:
        return None

    return pow(a, p - 1, p)


# ---------------------------------------------------------
# Euler's Totient Function
# ---------------------------------------------------------
def euler_totient(n):
    result = n
    p = 2
    temp = n

    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1

    if temp > 1:
        result -= result // temp

    return result


# ---------------------------------------------------------
# Part C: Euler's Theorem
# ---------------------------------------------------------
def euler_theorem(a, n):
    if euclid_gcd(a, n) != 1:
        return None

    phi = euler_totient(n)
    result = pow(a, phi, n)

    return phi, result


# ---------------------------------------------------------
# Part D: Chinese Remainder Theorem
# ---------------------------------------------------------
def chinese_remainder_theorem(remainders, moduli):

    # Check if moduli are pairwise coprime
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if euclid_gcd(moduli[i], moduli[j]) != 1:
                return None

    M = math.prod(moduli)
    result = 0

    for r, m in zip(remainders, moduli):

        Mi = M // m

        # Find modular inverse using Python
        inverse = pow(Mi, -1, m)

        result += r * Mi * inverse

    return result % M


# =========================================================
# MAIN PROGRAM
# =========================================================

print("=" * 55)
print("MODULAR ARITHMETIC ALGORITHMS")
print("FOR CRYPTOGRAPHIC COMPUTATIONS")
print("=" * 55)


# ---------------------------------------------------------
# Part A: Euclid's Algorithm
# ---------------------------------------------------------
print("\n--- Euclid's Algorithm ---")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = euclid_gcd(a, b)

print("GCD =", gcd)


# ---------------------------------------------------------
# Part B: Fermat's Little Theorem
# ---------------------------------------------------------
print("\n--- Fermat's Little Theorem ---")

a = int(input("Enter value of a: "))
p = int(input("Enter a prime number: "))

if euclid_gcd(a, p) == 1:

    result = fermat_little_theorem(a, p)

    print(f"{a}^({p}-1) mod {p} =", result)

    if result == 1:
        print("Fermat's Theorem verified.")

else:
    print("a and p must be coprime.")


# ---------------------------------------------------------
# Part C: Euler's Theorem
# ---------------------------------------------------------
print("\n--- Euler's Theorem ---")

a = int(input("Enter value of a: "))
n = int(input("Enter n for Euler's Theorem: "))

if euclid_gcd(a, n) == 1:

    phi, result = euler_theorem(a, n)

    print("Euler Totient phi(n) =", phi)
    print(f"{a}^phi({n}) mod {n} =", result)

    if result == 1:
        print("Euler's Theorem verified.")

else:
    print("a and n must be coprime.")


# ---------------------------------------------------------
# Part D: Chinese Remainder Theorem
# ---------------------------------------------------------
print("\n--- Chinese Remainder Theorem ---")

count = int(input("Enter number of congruences: "))

remainders = []
moduli = []

for i in range(count):

    r = int(input(f"Enter remainder {i + 1}: "))
    m = int(input(f"Enter modulus {i + 1}: "))

    remainders.append(r)
    moduli.append(m)


solution = chinese_remainder_theorem(remainders, moduli)

if solution is not None:

    print("\nRemainders =", remainders)
    print("Moduli =", moduli)
    print("CRT Solution =", solution)

    print("\nVerification:")

    for r, m in zip(remainders, moduli):
        print(
            f"{solution} mod {m} = {solution % m}"
        )

else:
    print("Error: Moduli must be pairwise coprime.")


print("\n" + "=" * 55)
print("PROGRAM EXECUTION COMPLETED")
print("=" * 55)