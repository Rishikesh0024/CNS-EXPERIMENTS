import matplotlib.pyplot as plt

ciphertext = "DWWDFNDWGDZQ"
ciphertext = ciphertext.replace(" ", "").upper()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = len(ciphertext)

print("\nFrequency Analysis Table:")
print("Letter  Count  Percentage")

frequency = []
for letter in letters:
    count = ciphertext.count(letter)
    frequency.append(count)
    percentage = (count / total) * 100
    print(letter, " ", count, " ", round(percentage, 2), "%")

plt.bar(letters, frequency)
plt.xlabel("Letters")
plt.ylabel("Frequency")
plt.title("Letter Frequency Analysis")
plt.show()

highest = max(frequency)
most_common = letters[frequency.index(highest)]

print("\nObservation")
print("Most frequent letter:", most_common)
print("Frequency:", highest)

print("\nResult:")
print("Frequency analysis of the ciphertext was successfully performed")