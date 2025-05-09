# Olympus Autogenesis Core – Self-evolving agent generator
from utils.autogenesis_utils import scan_for_gaps, generate_agent_blueprint

def run_autogenesis():
    print("🧬 Olympus Autogenesis Core engaged...")
    gaps = scan_for_gaps()
    for gap in gaps:
        generate_agent_blueprint(gap)
