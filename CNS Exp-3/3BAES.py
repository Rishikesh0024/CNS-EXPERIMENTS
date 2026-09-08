from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time

KEY = b"123456789Uabcdef"
IV = b"afcdef1234567890"

def encrypt_ecb(plaintext):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, AES.block_size))

def encrypt_cbc(plaintext):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    return cipher.encrypt(pad(plaintext, AES.block_size))

def encrypt_cfb(plaintext):
    cipher = AES.new(KEY, AES.MODE_CFB, IV)
    return cipher.encrypt(plaintext)

def encrypt_ofb(plaintext):
    cipher = AES.new(KEY, AES.MODE_OFB, IV)
    return cipher.encrypt(plaintext)

plaintext = input("Enter Plaintext: ").encode()
print("AES Encryption Results")

start = time.perf_counter()
ecb = encrypt_ecb(plaintext)
ecb_time = time.perf_counter() - start
print("ECB:")
print(ecb.hex())

start = time.perf_counter()
cbc = encrypt_cbc(plaintext)
cbc_time = time.perf_counter() - start
print("CBC:")
print(cbc.hex())

start = time.perf_counter()
cfb = encrypt_cfb(plaintext)
cfb_time = time.perf_counter() - start
print("CFB:")
print(cfb.hex())

start = time.perf_counter()
ofb = encrypt_ofb(plaintext)
ofb_time = time.perf_counter() - start
print("OFB:")
print(ofb.hex())

print("Execution Time")
print(f"ECB: {ecb_time:.8f} seconds")
print(f"CBC: {cbc_time:.8f} seconds")
print(f"CFB: {cfb_time:.8f} seconds")
print(f"OFB: {ofb_time:.8f} seconds")

print("Security Comparison")
print("ECB: Least secure")
print("CBC: High security")
print("CFB: High security (streaming)")
print("OFB: High security (No error propagation)")