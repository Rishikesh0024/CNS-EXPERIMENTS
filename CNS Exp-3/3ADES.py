from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import time

plaintext = b"CRYPTOGRAPHYLAB"

def pad(text):
    while len(text) % 8 != 0:
        text += b" "
    return text

plaintext = pad(plaintext)
key = get_random_bytes(8)
iv = get_random_bytes(8)

def encrypt(mode):
    start = time.time()
    if mode == DES.MODE_ECB:
        cipher = DES.new(key, mode)
    else:
        cipher = DES.new(key, mode, iv)
    ciphertext = cipher.encrypt(plaintext)
    end = time.time()
    return ciphertext.hex(), end - start

ecb_ct, ecb_time = encrypt(DES.MODE_ECB)
cbc_ct, cbc_time = encrypt(DES.MODE_CBC)
cfb_ct, cfb_time = encrypt(DES.MODE_CFB)
ofb_ct, ofb_time = encrypt(DES.MODE_OFB)

print("DES Encryption Results")
print(f"ECB Ciphertext:\n{ecb_ct}")
print(f"CBC Ciphertext:\n{cbc_ct}")
print(f"CFB Ciphertext:\n{cfb_ct}")
print(f"OFB Ciphertext:\n{ofb_ct}")
print("Execution Time")
print(f"ECB: {ecb_time:.6f} seconds")
print(f"CBC: {cbc_time:.6f} seconds")
print(f"CFB: {cfb_time:.6f} seconds")
print(f"OFB: {ofb_time:.6f} seconds")
print("Security Comparison")
print("ECB: Least secure")
print("CBC: Secure")
print("CFB: Secure for streaming")
print("OFB: Secure for noisy channels")
