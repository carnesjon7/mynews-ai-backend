# Themis.Audit: Compliance and legal safety monitor
from utils.audit_utils import scan_compliance_risks, report_to_zeus

def run_audit():
    risks = scan_compliance_risks()
    if risks:
        for risk in risks:
            report_to_zeus(risk)
    else:
        print("✅ Themis: No compliance risks found.")
