from tinyec import registry
from cryptography.hazmat.primitives.asymmetric import rsa
import secrets
import time

curve = registry.get_curve('secp256r1')

start_ecc = time.perf_counter()

private_key_ecc = secrets.randbelow(curve.field.n)
public_key_ecc = private_key_ecc * curve.g

ecc_time = time.perf_counter() - start_ecc

start_rsa = time.perf_counter()

private_key_rsa = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key_rsa = private_key_rsa.public_key()

rsa_time = time.perf_counter() - start_rsa

print("ECC AND RSA KEY GENERATION")
print("---------------------------")

print("\nECC Key Generation")
print("------------------")
print("Curve: secp256r1")
print("ECC Private Key:", private_key_ecc)
print("ECC Public Key X:", public_key_ecc.x)
print("ECC Public Key Y:", public_key_ecc.y)
print("ECC Key Generation Time:", ecc_time, "seconds")

print("\nRSA Key Generation")
print("------------------")
print("RSA Key Size: 2048 bits")
print("RSA Public Exponent:", public_key_rsa.public_numbers().e)
print("RSA Modulus:", public_key_rsa.public_numbers().n)
print("RSA Key Generation Time:", rsa_time, "seconds")

print("\nComputational Efficiency")
print("------------------------")

if ecc_time < rsa_time:
    print("ECC generated the key faster than RSA.")
else:
    print("RSA generated the key faster than ECC.")

print("\nECC uses a smaller key size while providing strong security.")