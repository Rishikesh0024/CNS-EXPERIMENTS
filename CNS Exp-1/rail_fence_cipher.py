def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for ch in text:
        fence[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return "".join("".join(r) for r in fence)

def rail_fence_decrypt(cipher, rails):
    n = len(cipher)
    pattern = []
    rail, direction = 0, 1
    for i in range(n):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    indices = sorted(range(n), key=lambda i: pattern[i])
    result = [''] * n
    for i, ch in zip(indices, cipher):
        result[i] = ch
    return "".join(result)

if __name__ == "__main__":
    text = input("Enter text: ")
    rails = int(input("Enter number of rails: "))
    encrypted = rail_fence_encrypt(text, rails)
    decrypted = rail_fence_decrypt(encrypted, rails)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
