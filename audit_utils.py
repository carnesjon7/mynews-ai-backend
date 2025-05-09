# Themis compliance checker
def scan_compliance_risks():
    return ["Email missing unsubscribe link", "Unverified affiliate income claim"]

def report_to_zeus(risk):
    print(f"⚠️ COMPLIANCE RISK: {risk}")
