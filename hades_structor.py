# Hades.Structor – Triggers full sovereignty shift at $10K/month
from utils.revenue_utils import get_monthly_revenue
from utils.sovereign_utils import prepare_entity_setup, launch_entity_migration

SOVEREIGN_TRIGGER = 10000

def run_hades():
    revenue = get_monthly_revenue()
    if revenue >= SOVEREIGN_TRIGGER:
        print(f"🔐 Hades Triggered: Monthly revenue at ${revenue}. Initiating Sovereign Shift Protocol.")
        entities = prepare_entity_setup()
        launch_entity_migration(entities)
    else:
        print(f"⏳ Sovereign Shift dormant. Revenue at ${revenue}. Waiting for $10K+.")
