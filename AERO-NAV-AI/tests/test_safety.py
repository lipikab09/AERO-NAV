import torch
from src.safety.uncertainty import UncertaintyEstimationLayer
from src.perception.panoptic import TraversabilityPerceptionModule

def test_uncertainty_estimation():
    layer = UncertaintyEstimationLayer({"safety": {"epistemic_uncertainty_threshold": 0.35}})
    model = TraversabilityPerceptionModule({"system": {"device": "cpu"}})
    ep, al, trigger = layer.estimate_uncertainty(model, torch.randn(1, 3, 256, 256), num_samples=2)
    assert isinstance(ep.item(), float)
