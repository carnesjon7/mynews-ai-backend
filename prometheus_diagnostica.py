# Diagnoses and fixes failing agents automatically
from utils.diagnostic_utils import scan_agent_health, auto_patch_agent, escalate_to_zeus

def run_diagnosis_cycle():
    failures = scan_agent_health()
    for issue in failures:
        if issue["autopatchable"]:
            auto_patch_agent(issue)
        else:
            escalate_to_zeus(issue)
