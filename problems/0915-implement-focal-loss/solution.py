import torch
import torch.nn.functional as F


def focal_loss(logits, targets, gamma=2.0):

    total_loss = 0

    for i in range(len(logits)):

        # Get one row
        row = logits[i]

        # Convert logits of this row into log probabilities
        log_probs = F.log_softmax(row, dim=0)

        # Get the correct class
        target = targets[i]

        # Get log probability of the correct class
        log_pt = log_probs[target]

        # Get probability of the correct class
        pt = torch.exp(log_pt)

        # Focal loss for this sample
        loss = -(1 - pt) ** gamma * log_pt

        total_loss += loss

    # Return mean loss
    return total_loss / len(logits)

