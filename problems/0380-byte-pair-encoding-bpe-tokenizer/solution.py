from collections import Counter
def byte_pair_encoding(corpus: dict, num_merges: int) -> list:
    """
    Train a BPE tokenizer on the given corpus.
    
    Args:
        corpus: Dictionary mapping space-separated token sequences to their frequencies.
                Example: {"l o w </w>": 5, "n e w </w>": 6}
        num_merges: Number of merge operations to perform.
    
    Returns:
        List of tuples, where each tuple contains the two tokens that were merged.
        Example: [('l', 'o'), ('lo', 'w')]
    """
    words = {tuple(word.split()):freq for word,freq in corpus.items()}
    merges = []
    for _ in range(num_merges):

        pair_counter = Counter()
        for tokens,freq in words.items():
            for i in range(len(tokens) - 1):
                if i + 1 < len(tokens):
                    pair = (tokens[i],tokens[i + 1])
                    pair_counter[pair] += freq

        best_pair = max(pair_counter,key = pair_counter.get)

        merges.append(best_pair)

        new_word = {}
        for token,freq in words.items():
            new_token =  []
            i = 0
            while i < len(token):
                if i < (len(token)) - 1 and token[i] == best_pair[0] and token[i + 1] == best_pair[1]:
                    new_token.append(token[i] + token[i + 1])
                    i += 2
                else:
                    new_token.append(token[i])
                    i +=1 
            new_word[tuple(new_token)] = freq
        words = new_word
    return merges

