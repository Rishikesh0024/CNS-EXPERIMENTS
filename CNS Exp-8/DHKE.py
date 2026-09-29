p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter private key of User A: "))
b = int(input("Enter private key of User B: "))

A = pow(g, a, p)
B = pow(g, b, p)

print("\nPublic Key Exchange")
print("-------------------")
print("User A Public Key:", A)
print("User B Public Key:", B)

shared_key_A = pow(B, a, p)
shared_key_B = pow(A, b, p)

print("\nShared Session Key")
print("------------------")
print("User A Shared Key:", shared_key_A)
print("User B Shared Key:", shared_key_B)

print("\nVerification")
print("------------")

if shared_key_A == shared_key_B:
    print("Both users have generated the same shared key.")
    print("Secure Session Key Established")
else:
    print("Shared keys are different.")
    print("Key Exchange Failed")