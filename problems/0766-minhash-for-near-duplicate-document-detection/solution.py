import numpy as np
import hashlib


def minhash_near_duplicates(
    documents: list[str],
    num_hashes: int,
    threshold: float,
    shingle_size: int,
    seed: int
) -> list[tuple]:
    """
    Detect near-duplicate document pairs using MinHash.

    Returns a list of (i, j) index pairs (i < j) whose estimated Jaccard
    similarity meets or exceeds the given threshold.
    """

    # Large prime
    p = 2**61 - 1

    # Generate random hash parameters
    rng = np.random.default_rng(seed)

    a = rng.integers(1, p, size=num_hashes, dtype=np.int64)
    b = rng.integers(0, p, size=num_hashes, dtype=np.int64)

    # --------------------------------------------------
    # 1. Create shingle sets
    # --------------------------------------------------

    shingles_set = []

    for doc in documents:
        tokens = doc.lower().split()

        if not tokens:
            shingles_set.append(set())
            continue

        # If document is shorter than shingle size
        if len(tokens) < shingle_size:
            shingles = {" ".join(tokens)}

        else:
            shingles = set()

            for i in range(len(tokens) - shingle_size + 1):
                shingle = " ".join(tokens[i:i + shingle_size])
                shingles.add(shingle)

        shingles_set.append(shingles)

    # --------------------------------------------------
    # 2. Create MinHash signatures
    # --------------------------------------------------

    signatures = []

    for shingles in shingles_set:

        # Use p as initial value
        signature = np.full(num_hashes, p, dtype=np.int64)

        for shingle in shingles:

            # Convert shingle to deterministic integer
            digest = hashlib.md5(
                shingle.encode("utf-8")
            ).hexdigest()

            base = int(digest, 16) % p

            # Apply all hash functions
            hashes = (a * base + b) % p

            # Take minimum value for each hash function
            signature = np.minimum(signature, hashes)

        signatures.append(signature)

    # --------------------------------------------------
    # 3. Estimate Jaccard similarity
    # --------------------------------------------------

    result = []

    for i in range(len(documents)):

        for j in range(i + 1, len(documents)):

            similarity = np.mean(
                signatures[i] == signatures[j]
            )

            if similarity >= threshold:
                result.append((i, j))

    return result



        
