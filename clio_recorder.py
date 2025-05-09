# Records affiliate payouts and revenue flow securely
ledger = []

def record_transaction(amount, source, tier2=None):
    ledger.append({
        "amount": amount,
        "source": source,
        "tier2": tier2,
        "status": "processed"
    })
    print(f"📜 Clio: Transaction recorded — ${amount} from {source}. Tier 2: {tier2}")
