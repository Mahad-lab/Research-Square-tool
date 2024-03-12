from itertools import combinations
import math

query = "python js html css react"
n = len(query.split())
k = n


def generate_combinations(query, min_words=1):
    words = query.split()
    combinations_list = []
    for r in range(min_words, len(words) + 1):
        for subset in combinations(words, r):
            combinations_list.append(' '.join(subset))
    return combinations_list


words = generate_combinations(query)
print(len(words))
print(words)

# n, k = 3,3
# Print total number of possible combinations
s = 0
for i in range(1, n+1):
    s += math.comb(n, i)
print(s)
# print(math.comb(n, k)) 