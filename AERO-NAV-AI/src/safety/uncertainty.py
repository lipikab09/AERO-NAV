import torch
import torch.nn as nn
from typing import Dict, Tuple

class UncertaintyEstimationLayer:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.epistemic_thresh = config.get("safety", {}).get("epistemic_uncertainty_threshold", 0.35)

    def estimate_uncertainty(self, model: nn.Module, inputs: torch.Tensor, num_samples: int = 10) -> Tuple[torch.Tensor, torch.Tensor, bool]:
        model.train()
        predictions = []
        with torch.no_grad():
            for _ in range(num_samples):
                output = model(inputs)
                predictions.append(torch.softmax(output["segmentation_logits"], dim=1))
        stack = torch.stack(predictions)
        epistemic = torch.var(stack, dim=0).mean()
        aleatoric = torch.tensor(0.15)
        trigger = epistemic.item() > self.epistemic_thresh
        return epistemic, aleatoric, trigger
