
def normalization(string):
    string = string.lower()
    string = string.split()
    normalized_str = []

    for word in string:
        if word == 'a' or word == 'an' or word == 'the':
            continue

        # Keep only alphanumeric characters
        word = ''.join(c for c in word if c.isalnum())

        if word:
            normalized_str.append(word)

    return " ".join(normalized_str)


def evaluate_corpus_qa(corpus_length, questions):
    if not questions:
        return [0.0, 0.0, 0.0, 0.0]

    early_correct = mid_correct = late_correct = 0
    early_total = mid_total = late_total = 0

    for doc in questions:
        position = doc['position']
        gold = doc['gold']
        pred = doc['pred']

        normalized_gold = normalization(gold)
        normalized_pred = normalization(pred)

        if position < corpus_length / 3:
            early_total += 1
            if normalized_gold == normalized_pred:
                early_correct += 1

        elif position < 2 * (corpus_length / 3):
            mid_total += 1
            if normalized_gold == normalized_pred:
                mid_correct += 1

        else:
            late_total += 1
            if normalized_gold == normalized_pred:
                late_correct += 1

    overall_em = (early_correct + mid_correct + late_correct) / len(questions)

    early_acc = early_correct / early_total if early_total else 0.0
    mid_acc = mid_correct / mid_total if mid_total else 0.0
    late_acc = late_correct / late_total if late_total else 0.0

    return [overall_em, early_acc, mid_acc, late_acc]

