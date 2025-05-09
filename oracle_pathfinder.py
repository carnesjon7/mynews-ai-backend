# Oracle.Pathfinder: Strategic long-horizon global trend forecaster
from utils.trend_utils import scan_global_trends, evaluate_threats

def run_oracle():
    shifts = scan_global_trends()
    evaluate_threats(shifts)
