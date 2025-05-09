# Aether.Proxy: Legal and operational proxy for automated filings
from utils.legal_utils import check_filing_status, file_documents, monitor_ip

def run_aether():
    check_filing_status()
    file_documents()
    monitor_ip()
