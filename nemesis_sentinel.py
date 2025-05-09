# Nemesis.Sentinel: Personal digital security agent
from utils.privacy_utils import search_sensitive_data, submit_removal_requests, escalate_to_zeus
from utils.revenue_utils import get_monthly_revenue

def run_sentinel():
    revenue = get_monthly_revenue()
    frequency = "daily" if revenue >= 15000 else "weekly"
    print(f"Nemesis running in {frequency} mode...")

    threats = search_sensitive_data()
    for threat in threats:
        if threat['severity'] == 'high':
            escalate_to_zeus(threat)
        else:
            submit_removal_requests(threat)
