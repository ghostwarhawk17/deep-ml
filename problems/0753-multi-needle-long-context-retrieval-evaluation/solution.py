def evaluate_mrcr(tasks, buckets):
    """
    Compute per-bucket mean match rate for multi-needle retrieval tasks.
    """

    scores = [[] for _ in buckets]          # FIX 1: outside task loop

    for task in tasks:
        expected = task["expected"]          # FIX 2
        predicted = task["predicted"]        # FIX 2

        expectedset = set(expected)
        predictedset = set(predicted)

        context_length = task["context_length"]   # FIX 2

        common = expectedset & predictedset
        rate = len(common) / len(expectedset)      # FIX 3

        for i, bucket in enumerate(buckets):
            if bucket >= context_length:
                scores[i].append(rate)
                break

    bucket_score = []

    for score in scores:
        if not score:
            bucket_score.append(0.0)
        else:
            bucket_score.append(
                round(sum(score) / len(score), 4)   # FIX 4
            )

    return bucket_score
            