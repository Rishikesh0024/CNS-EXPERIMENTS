import random, string

def generate_key():
    shuffled = list(string.ascii_lowercase)
    random.shuffle(shuffled)
    return dict(zip(string.ascii_lowercase, shuffled))

def monoalphabetic_encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            enc = key[ch.lower()]
            result += enc.upper() if ch.isupper() else enc
        else:
            result += ch
    return result

def monoalphabetic_decrypt(text, key):
    reverse_key = {v: k for k, v in key.items()}
    result = ""
    for ch in text:
        if ch.isalpha():
            dec = reverse_key[ch.lower()]
            result += dec.upper() if ch.isupper() else dec
        else:
            result += ch
    return result

if __name__ == "__main__":
    text = input("Enter text: ")
    key = generate_key()
    print(f"Key: {key}")
    encrypted = monoalphabetic_encrypt(text, key)
    decrypted = monoalphabetic_decrypt(encrypted, key)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
