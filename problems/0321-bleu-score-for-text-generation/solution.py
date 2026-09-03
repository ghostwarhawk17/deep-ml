from collections import Counter
import math


def bleu_score(candidate, references, max_n):
    # If the candidate sentence is empty,
    # its BLEU score is 0.
    if not candidate:
        return 0.0

    # This list will store the precision for each n-gram size.
    # For example, if max_n = 4:
    # precisions = [1-gram precision, 2-gram precision,
    #               3-gram precision, 4-gram precision]
    precisions = []

    # Calculate precision for n = 1, 2, ..., max_n
    for n in range(1, max_n + 1):

        # ---------------------------------------------------------
        # STEP 1: Count n-grams in the candidate
        # ---------------------------------------------------------
        #
        # Example:
        # candidate = ["the", "cat", "sat"]
        # n = 2
        #
        # Candidate bigrams:
        # ("the", "cat")
        # ("cat", "sat")
        #
        # Counter stores how many times each n-gram appears.
        cand = Counter(
            tuple(candidate[i:i+n])
            for i in range(len(candidate) - n + 1)
        )

        # ---------------------------------------------------------
        # STEP 2: Find the maximum count of each n-gram
        # across all reference sentences
        # ---------------------------------------------------------
        #
        # BLEU uses "clipped precision".
        # If an n-gram occurs many times in the candidate,
        # we cannot count more occurrences than appear in
        # the references.
        #
        # Example:
        # Candidate contains "the" 3 times.
        # Reference 1 contains "the" 1 time.
        # Reference 2 contains "the" 2 times.
        #
        # Maximum reference count = 2.
        # Therefore, at most 2 occurrences can be counted
        # as matches.

        ref_counts = Counter()

        # Look at every reference sentence.
        for ref in references:

            # Count n-grams in this reference.
            r = Counter(
                tuple(ref[i:i+n])
                for i in range(len(ref) - n + 1)
            )

            # For every n-gram in this reference,
            # keep the largest count found among all references.
            for gram in r:
                ref_counts[gram] = max(
                    ref_counts[gram],
                    r[gram]
                )

        # ---------------------------------------------------------
        # STEP 3: Calculate clipped matches
        # ---------------------------------------------------------
        #
        # For every candidate n-gram:
        #
        # min(candidate_count, reference_count)
        #
        # This prevents an n-gram from being counted more times
        # than it occurs in the references.

        matches = sum(
            min(c, ref_counts[g])
            for g, c in cand.items()
        )

        # Total number of n-grams in the candidate.
        total = sum(cand.values())

        # If there are no matching n-grams,
        # BLEU becomes 0.
        #
        # This is important because if any n-gram precision is 0,
        # the geometric mean will also become 0.
        if matches == 0:
            return 0.0

        # Calculate precision for this n-gram size.
        #
        # Example:
        # 3 matching bigrams / 5 total bigrams = 0.6
        precisions.append(matches / total)

    # -------------------------------------------------------------
    # STEP 4: Find the closest reference length
    # -------------------------------------------------------------
    #
    # BLEU compares the candidate length with the reference
    # length that is closest to it.
    #
    # If two references are equally close,
    # the shorter one is selected.

    c_len = len(candidate)

    r_len = min(
    (len(r) for r in references),
    key=lambda x: (abs(x - c_len), x)
)

    # -------------------------------------------------------------
    # STEP 5: Calculate Brevity Penalty (BP)
    # -------------------------------------------------------------
    #
    # If the candidate is at least as long as the closest
    # reference, there is no penalty.
    #
    # BP = 1
    #
    # If the candidate is shorter, it receives a penalty:
    #
    # BP = exp(1 - reference_length / candidate_length)
    #
    # This prevents a very short sentence from getting
    # a high BLEU score just by matching a few words.

    bp = (
        1
        if c_len >= r_len
        else math.exp(1 - r_len / c_len)
    )

    # -------------------------------------------------------------
    # STEP 6: Calculate the geometric mean of precisions
    # -------------------------------------------------------------
    #
    # Suppose:
    # precisions = [0.8, 0.6, 0.5, 0.4]
    #
    # BLEU does NOT use the normal arithmetic average.
    # It uses the geometric mean:
    #
    # (0.8 × 0.6 × 0.5 × 0.4) ^ (1/4)
    #
    # math.prod(precisions) multiplies all precisions together.
    #
    # 1 / max_n takes the n-th root.

    score = math.prod(precisions) ** (1 / max_n)

    # -------------------------------------------------------------
    # STEP 7: Final BLEU score
    # -------------------------------------------------------------
    #
    # Final BLEU =
    # Brevity Penalty × Geometric Mean of n-gram precisions

    return bp * score