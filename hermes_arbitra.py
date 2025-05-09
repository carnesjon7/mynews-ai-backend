# Hermes.Arbitra: Business acquisition & flipping agent
from utils.market_utils import find_opportunities, run_due_diligence, simulate_roi, trigger_acquisition
from utils.revenue_utils import get_monthly_revenue

def run_arbitra():
    revenue = get_monthly_revenue()
    if revenue < 20000:
        print("Revenue threshold not met. Arbitra dormant.")
        return

    targets = find_opportunities()
    for target in targets:
        if run_due_diligence(target):
            projection = simulate_roi(target)
            if projection['roi'] >= 2.0:
                trigger_acquisition(target, projection)
