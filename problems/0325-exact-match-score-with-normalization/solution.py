import string

def exact_match_score(predictions: list[str], references: list[str]) -> float:
    """
    Calculate the exact match score between predictions and references.
    
    Args:
        predictions: List of predicted strings
        references: List of reference (ground truth) strings
    
    Returns:
        Exact match score as a float between 0 and 1
    """
    # Your code here
    
    normalized = []
    for word in predictions:
        word_norm  = ""
        for char in word:
            if char.isalpha() and char.isupper():
                char = char.lower()
                word_norm += char
            elif char.isalpha() and char.islower():
                word_norm += char
            elif char.isdigit():
                word_norm += char
            else:
                continue

        normalized.append(word_norm)
    normalized1 = []
    for word in references:
        word_norm1  = ""
        for char in word:
            if char.isalpha() and char.isupper():
                char = char.lower()
                word_norm1 += char
            elif char.isalpha() and char.islower():
                word_norm1 += char
            elif char.isdigit():
                word_norm1 += char
            else:
                continue
        normalized1.append(word_norm1)

    ref_count = set(normalized1)
    count = 0
    for word in normalized:
        if word in normalized1:       # don't use set
            count += 1
    return count / len(predictions) if count > 0 else 0.0

        
                

            
            

