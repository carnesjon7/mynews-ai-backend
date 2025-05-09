# Gaia II – Global real estate acquisition and dynasty builder
from utils.property_utils import scan_global_properties, secure_acquisition
from utils.revenue_utils import get_monthly_revenue

REVENUE_TRIGGER = 100000

def run_gaia_dynasty():
    revenue = get_monthly_revenue()
    if revenue >= REVENUE_TRIGGER:
        print(f"🌍 Gaia II Activated: Monthly revenue at ${revenue}")
        properties = scan_global_properties()
        for prop in properties:
            secure_acquisition(prop)
    else:
        print(f"⏳ Gaia II dormant. Waiting for $100K+ revenue.")
