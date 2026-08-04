def vigenere_encrypt(text, key):
    result, key = "", key.lower()
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
            ki += 1
        else:
            result += ch
    return result

def vigenere_decrypt(text, key):
    result, key = "", key.lower()
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('a')
            result += chr((ord(ch) - base - shift) % 26 + base)
            ki += 1
        else:
            result += ch
    return result

if __name__ == "__main__":
    text = input("Enter text: ")
    key = input("Enter key: ")
    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
