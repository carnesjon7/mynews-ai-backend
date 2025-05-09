# Sovereign Ascension: Governance Core Protocol
from utils.governance_utils import initiate_governance_planning
from utils.revenue_utils import get_retained_capital

TRIGGER_THRESHOLD = 100_000_000  # $100 million

def run_ascension():
    capital = get_retained_capital()
    if capital >= TRIGGER_THRESHOLD:
        print(f"👑 Sovereign Ascension Triggered: Retained Capital at ${capital}")
        initiate_governance_planning()
    else:
        print(f"⏳ Sovereign Ascension dormant. Capital at ${capital}. Waiting for $100M+.")
