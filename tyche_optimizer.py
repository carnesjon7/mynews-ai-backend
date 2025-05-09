# Tyche.Optimizer: Revenue optimization and pricing strategist
from utils.optimize_utils import analyze_pricing, suggest_adjustments

def run_optimizer():
    suggestions = analyze_pricing()
    for s in suggestions:
        suggest_adjustments(s)
