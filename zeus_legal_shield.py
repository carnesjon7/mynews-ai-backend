# Legal Adaptation Shield – Monitors global laws and ensures compliance
from utils.legal_monitor_utils import scan_legislation_changes, flag_risk_activity

def run_legal_shield():
    print("🛡 Zeus Legal Shield online...")
    laws = scan_legislation_changes()
    for law in laws:
        flag_risk_activity(law)
