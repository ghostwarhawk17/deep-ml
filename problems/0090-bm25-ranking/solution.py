import numpy as np
import math
from collections import Counter

def calculate_bm25_scores(corpus, query, k1=1.5, b=0.75):
    if not corpus:
        return []

    N = len(corpus)
    df_word = Counter()

    for doc in corpus:
        for word in set(doc):
            df_word[word] += 1

    avgdl = sum(len(doc) for doc in corpus) / N

    scores = []

    for doc in corpus:
        word_count = Counter(doc)
        doc_len = len(doc)
        score = 0

        for word in query:
            tf = word_count[word]

            # IDF expected by this problem
            idf = math.log((N + 1) / (df_word[word] + 1))

            tfid = idf * (
                (tf * (k1 + 1)) /
                (tf + k1 * (1 - b + b * doc_len / avgdl))
            )

            score += tfid

        scores.append(round(score, 3))

    return scores


