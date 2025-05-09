# Utility to detect legal changes and flag agent functions
def scan_legislation_changes():
    print("📜 Scanning jurisdictions for new AI-related laws...")
    return [
        {"country": "UK", "law": "AI registration bill", "risk": "High"},
        {"country": "Canada", "law": "Agent transparency law", "risk": "Moderate"},
    ]

def flag_risk_activity(law):
    print(f"⚠️ Law risk detected: {law['law']} in {law['country']} — Flagging agent activity.")
