# Erebus.CreditReform Protocol – Tier 1 and Tier 2 Logic
from utils.credit_utils import run_dispute_injection, run_infra_update, secure_scrub

def execute_credit_reform():
    print("📈 Erebus.CreditReform ACTIVATED")
    run_dispute_injection()
    run_infra_update()
    secure_scrub()
