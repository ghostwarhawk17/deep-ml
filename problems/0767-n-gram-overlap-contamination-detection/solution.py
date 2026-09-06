def detect_contamination(test_examples, train_corpus, n, threshold):
    """
    Args:
        test_examples: list[str] - test set documents
        train_corpus: list[str] - training set documents
        n: int - n-gram size
        threshold: float - coverage ratio in [0, 1]

    Returns:
        float - contamination percentage in [0, 100]
    """

    train_ngrams = set()

    for document in train_corpus:
        tokens = document.split()

        for i in range(len(tokens) - n + 1):
            train_ngrams.add(tuple(tokens[i:i + n]))

    contaminated = 0

    # Check each test example
    for document in test_examples:
        tokens = document.split()
        L = len(tokens)

        if L == 0:
            continue

        covered = [False] * L

        for i in range(L - n + 1):
            window = tuple(tokens[i:i + n])

            if window in train_ngrams:
                for j in range(i, i + n):
                    covered[j] = True

        coverage = sum(covered) / L

        if coverage >= threshold:
            contaminated += 1

    if len(test_examples) == 0:
        return 0.0

    return (contaminated / len(test_examples)) * 100