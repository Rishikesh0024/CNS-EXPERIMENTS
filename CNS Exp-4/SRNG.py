import secrets
import numpy as np
from scipy.stats import chisquare

n = 100
random_numbers = [secrets.randbelow(10) for _ in range(n)]
numbers = np.array(random_numbers)

mean = np.mean(numbers)
variance = np.var(numbers)

observed_frequency = np.bincount(numbers, minlength=10)
expected_frequency = np.full(10, n / 10)

chi_square_statistic, p_value = chisquare(observed_frequency, expected_frequency)

print("Generated Random Numbers:")
print(numbers)
print("\nStatistical Analysis")
print("Mean:", round(mean, 3))
print("Variance:", round(variance, 3))
print("Observed frequency")
print(observed_frequency.astype(int))
print("Expected frequency")
print(expected_frequency.astype(int))
print("Chi-square Statistic:", round(chi_square_statistic, 2))
print("P-value:", round(p_value, 2))