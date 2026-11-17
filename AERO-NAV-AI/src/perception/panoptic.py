import torch
import torch.nn as nn
from typing import Dict, Any

class TraversabilityPerceptionModule(nn.Module):
    def __init__(self, config: Dict[str, Any]):
        super().__init__()
        self.config = config
        self.device = torch.device(config.get("system", {}).get("device", "cpu"))
        self.backbone = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.AdaptiveAvgPool2d((128, 128))
        ).to(self.device)
        self.classifier = nn.Conv2d(64, 5, kernel_size=1).to(self.device)

    def forward(self, rgb_image: torch.Tensor) -> Dict[str, torch.Tensor]:
        rgb_image = rgb_image.to(self.device)
        features = self.backbone(rgb_image)
        logits = self.classifier(features)
        segmentation_mask = torch.argmax(logits, dim=1)
        costmap = torch.where((segmentation_mask == 3), torch.tensor(0.0, device=self.device), torch.tensor(1.0, device=self.device))
        return {"segmentation_logits": logits, "segmentation_mask": segmentation_mask, "traversability_costmap": costmap}
