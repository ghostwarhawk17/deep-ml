import torch
import torch.nn.functional as F

def mtp_loss(main_logits, main_targets, mtp_logits, mtp_targets, mtp_weight):

    main_logits = torch.tensor(main_logits, dtype=torch.float32)
    main_targets = torch.tensor(main_targets, dtype=torch.long)

    mtp_logits = torch.tensor(mtp_logits, dtype=torch.float32)
    mtp_targets = torch.tensor(mtp_targets, dtype=torch.long)

    # Cross entropy for main LM head
    main_loss = F.cross_entropy(main_logits, main_targets)

    # Cross entropy for MTP head
    mtp_loss = F.cross_entropy(mtp_logits, mtp_targets)

    # Total loss
    loss = main_loss + mtp_weight * mtp_loss

    return round(loss.item(), 6)