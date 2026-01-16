def pairwise_preference_judge(comparisons: list, criteria_weights: dict, tie_threshold: float) -> dict:
    """
    Analyze pairwise comparisons between LLM responses.
    """

    # Handle empty input
    if not comparisons:
        return {
            'results': [],
            'win_rate_a': 0.0,
            'win_rate_b': 0.0,
            'tie_rate': 0.0,
            'avg_margin': 0.0
        }

    # Normalize weights so they sum to 1
    total_weight = sum(criteria_weights.values())
    normalized_weights = {
        k: v / total_weight for k, v in criteria_weights.items()
    }

    results = []
    wins_a = wins_b = ties = 0
    total_margin = 0.0

    for comp in comparisons:
        weighted_a = 0.0
        weighted_b = 0.0

        # Compute weighted scores
        for criterion, weight in normalized_weights.items():
            weighted_a += comp['scores_a'][criterion] * weight
            weighted_b += comp['scores_b'][criterion] * weight

