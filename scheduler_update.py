# Optional scheduler snippet reflecting the two-phase protocol
from agents.hermes_arbitra import run_arbitra
from utils.revenue_utils import get_monthly_revenue

def run_phase_switch():
    revenue = get_monthly_revenue()
    if revenue >= 50000:
        print("🏛 Empire mode triggered. Running Hermes.Arbitra...")
        run_arbitra()
    else:
        print("🚀 Still in Acceleration Mode. Arbitra dormant.")
