import random
import math
import matplotlib.pyplot as plt

# Srouce
symbols = ['a', 'b', 'c']
prob = 1 / 3  # porb of each symbol
entropy = -3 * (prob * math.log2(prob))  # Entropy

# Set of possible codewords
codeword_set = ['0', '1', '00', '01', '10', '11']

# Simulation parameters
num_trials = 10000
prefix_free_lengths = []
non_prefix_free_lengths = []

def is_prefix_free(codebook):
    codewords = list(codebook.values())
    for i in range(len(codewords)):
        for j in range(len(codewords)):
            if i != j and codewords[j].startswith(codewords[i]):
                return False
    return True

for _ in range(num_trials):
    # Randomly assign 3 unique codewords to a, b, c
    assigned = random.sample(codeword_set, 3)
    codebook = dict(zip(symbols, assigned))
    avg_len = sum(len(codebook[s]) * prob for s in symbols)

    if is_prefix_free(codebook):
        prefix_free_lengths.append(avg_len)
    else:
        non_prefix_free_lengths.append(avg_len)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(prefix_free_lengths, bins=20, alpha=0.7, label='Prefix-Free Codes', color='green')
plt.hist(non_prefix_free_lengths, bins=20, alpha=0.5, label='Non-Prefix-Free Codes', color='red')
plt.axvline(x=entropy, color='blue', linestyle='--', label=f'Entropy ≈ {entropy:.3f} bits')
plt.xlabel('Average Codeword Length (bits)')
plt.ylabel('Frequency')
plt.title('Histogram of Average Codeword Lengths\n(Prefix-Free vs Non-Prefix-Free)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
