from collections import defaultdict

def dup_ngram_ratio(text: str, n: int) -> float:
    tokens = text.split()
    n_grams = []

    window_size = n
    total_len = len(tokens) - window_size + 1

    if total_len <= 0:
        return 0.0

    for i in range(total_len):
        window_str = tokens[i:i + window_size]
        n_grams.append(tuple(window_str))

    freq = defaultdict(int)
    duplicates = 0

    for string in n_grams:
        freq[string] += 1

    for ngram in n_grams:
        if freq[ngram] > 1:
            duplicates += 1

    return round(duplicates / total_len, 4)