# Utilities for scanning and patching outdated agents
def scan_codebase():
    return ["athena_autopilot.py", "hera_billing.py"]

def fetch_updates(agent):
    print(f"📡 Fetching latest patch for {agent}")
    return {"approved": True, "changelog": "Improved exception handling"}

def apply_patch(agent, update_info):
    print(f"✅ Patched {agent} with: {update_info['changelog']}")

def notify_zeus(agent, update_info):
    print(f"⚠️ Update for {agent} requires Zeus approval: {update_info['changelog']}")
