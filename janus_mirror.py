# Janus.Mirror: Simulated failure and attack agent
from utils.simulation_utils import simulate_outage, simulate_api_throttle, simulate_affiliate_fraud

def run_mirror_test():
    simulate_outage()
    simulate_api_throttle()
    simulate_affiliate_fraud()
    print("🔁 Janus simulation completed.")
