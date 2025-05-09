# Monitors all public-facing links and endpoints
from utils.link_utils import check_critical_links

def run_linkwatch():
    failures = check_critical_links()
    for fail in failures:
        print(f"LINK FAIL: {fail['url']} — {fail['status']}")
