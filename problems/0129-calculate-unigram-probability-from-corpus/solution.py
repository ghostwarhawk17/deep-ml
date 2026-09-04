def unigram_probability(corpus: str, word: str) -> float:
    words = corpus.split()

    word_count = 0
    for cword in words:
        if cword == word:
            word_count += 1

    return word_count / len(words)
