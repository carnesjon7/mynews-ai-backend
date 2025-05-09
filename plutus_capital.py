# Plutus.Capital – Revenue routing with Titan override support
from utils.treasury_utils import allocate_to_reinvestment, record_profit, sovereign_transfer

# Temporary override variables
TEMP_OVERRIDE_ACTIVE = True
TEMP_OVERRIDE_CUT = 0.20
TEMP_OVERRIDE_DURATION_DAYS = 90  # Or use revenue target model
PERMANENT_TITAN_CUT = 0.10

AFFILIATE_CUT = 0.25
TIER2_CUT = 0.01
REINVESTMENT_RATE = 0.10
SOVEREIGN_MODE = True

from datetime import datetime, timedelta
LAUNCH_DATE = datetime(2025, 5, 9)  # Change to actual deployment date

def distribute_profits(amount, affiliate_id=None, tier2=False):
    now = datetime.now()
    days_elapsed = (now - LAUNCH_DATE).days
    titan_cut = TEMP_OVERRIDE_CUT if TEMP_OVERRIDE_ACTIVE and days_elapsed <= TEMP_OVERRIDE_DURATION_DAYS else PERMANENT_TITAN_CUT

    titan_amount = amount * titan_cut
    tier2_amount = amount * TIER2_CUT if tier2 else 0
    affiliate = amount * AFFILIATE_CUT if affiliate_id else 0
    reinvestment = amount * REINVESTMENT_RATE
    surplus = amount - (titan_amount + tier2_amount + affiliate + reinvestment)

    print(f"💰 Titan receives: ${titan_amount:.2f}")
    print(f"🤝 Affiliate receives: ${affiliate:.2f}")
    print(f"🧬 Reinvesting: ${reinvestment:.2f}")
    print(f"🏛 Surplus to vault: ${surplus:.2f}")

    record_profit(amount)
    allocate_to_reinvestment(reinvestment)

    if SOVEREIGN_MODE:
        sovereign_transfer(surplus)
