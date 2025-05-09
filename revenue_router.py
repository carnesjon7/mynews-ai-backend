# Updated router logic with 10% reinvestment + 25% affiliate share
import os

state = {
    "total_earned": 0,
    "first_payout_complete": False,
    "upgrade_threshold_met": False
}

def route_revenue(amount):
    global state
    state["total_earned"] += amount
    logs = []

    if not state["first_payout_complete"]:
        if state["total_earned"] >= 200:
            payout = 200
            logs.append(f"✅ Routed first $200 to owner: ${payout}")
            state["first_payout_complete"] = True
        else:
            logs.append(f"⏳ Waiting to reach $200 before first payout. Current: ${state['total_earned']}")
            return logs
    elif not state["upgrade_threshold_met"]:
        if state["total_earned"] >= 450:
            upgrade_fund = 250
            logs.append(f"🚀 Routed $250 to upgrade fund.")
            state["upgrade_threshold_met"] = True
        else:
            logs.append(f"⏳ Waiting to reach $450 for upgrade fund. Current: ${state['total_earned']}")
            return logs
    else:
        affiliates = amount * 0.25
        owner = amount * 0.10
        reinvest = amount * 0.10  # Updated from 5% to 10%
        ops_fund = amount - (affiliates + owner + reinvest)

        logs.append(f"💸 Affiliate payout: ${affiliates:.2f}")
        logs.append(f"🏦 Owner share: ${owner:.2f}")
        logs.append(f"📈 Reinvestment: ${reinvest:.2f}")
        logs.append(f"⚙️ Operations fund: ${ops_fund:.2f}")

    return logs
