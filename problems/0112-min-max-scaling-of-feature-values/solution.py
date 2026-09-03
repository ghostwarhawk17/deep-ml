def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    ans = []
    min_val = min(x)
    max_val = max(x)
    for n in x:
        ans.append((n - min_val)/ (max_val - min_val))

    return ans