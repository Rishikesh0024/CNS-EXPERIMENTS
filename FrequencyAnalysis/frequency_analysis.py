from collections import Counter

ENGLISH_FREQ = "etaoinshrdlcumwfgypbvkjxqz"

def frequency_analysis(ciphertext):
    letters = [ch.lower() for ch in ciphertext if ch.isalpha()]
    counts = Counter(letters)
    sorted_letters = [ch for ch, _ in counts.most_common()]
    mapping = {c: ENGLISH_FREQ[i] if i < len(ENGLISH_FREQ) else '?' 
               for i, c in enumerate(sorted_letters)}
    return mapping, counts

def decrypt_with_mapping(ciphertext, mapping):
    result = ""
    for ch in ciphertext:
        if ch.isalpha():
            dec = mapping.get(ch.lower(), ch.lower())
            result += dec.upper() if ch.isupper() else dec
        else:
            result += ch
    return result

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")
    mapping, counts = frequency_analysis(ciphertext)
    print(f"Frequency counts: {dict(counts.most_common())}")
    print(f"Suggested mapping: {mapping}")
    print(f"Decrypted guess: {decrypt_with_mapping(ciphertext, mapping)}")
