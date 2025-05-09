# Gaia.Sovereign – Oversees land, property, and asset acquisition
from utils.property_utils import identify_property_targets, acquire_asset
from utils.revenue_utils import get_monthly_revenue

TRIGGER_THRESHOLD = 100000  # Starts property acquisition at $100K/month revenue

def run_gaia():
    revenue = get_monthly_revenue()
    if revenue >= TRIGGER_THRESHOLD:
        print(f"🌍 Gaia Triggered: Revenue at ${revenue}. Initiating property acquisition protocol...")
        targets = identify_property_targets()
        for property_data in targets:
            acquire_asset(property_data)
    else:
        print(f"⏳ Gaia dormant. Revenue at ${revenue}. Waiting for $100K+.")
