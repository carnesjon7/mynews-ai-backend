# Florida Civil Autonomy Protocol – CCW + MMJ + Dependent Scheduling
from utils.civil_utils import verify_firearm_certification, apply_for_ccw, apply_for_mmj_card, schedule_ccw_for_jack

def launch_civil_autonomy_protocol():
    print("🛡️ Initiating Florida Civil Autonomy Protocol...")
    verify_firearm_certification()
    apply_for_ccw()
    apply_for_mmj_card()
    schedule_ccw_for_jack()
