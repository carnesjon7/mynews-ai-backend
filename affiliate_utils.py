# Handles payout logic for affiliates and Tier 2 agents
TIER_2_DIRECTORY = {
    "Z3A72": {"wallet": "anon_wallet_1", "active": True},
    "D4C19": {"wallet": "anon_wallet_2", "active": True}
}

def process_affiliate_payout(transaction_amount, affiliate_id, tier2=False):
    main_cut = transaction_amount * 0.10  # 10% to Titan
    tier2_cut = transaction_amount * 0.01 if tier2 else 0

    print(f"💰 Paying 10% to Titan (secure route)... Amount: ${main_cut:.2f}")
    if tier2 and affiliate_id in TIER_2_DIRECTORY and TIER_2_DIRECTORY[affiliate_id]["active"]:
        print(f"💰 Paying 1% to Tier 2 ({affiliate_id}) at {TIER_2_DIRECTORY[affiliate_id]['wallet']}... Amount: ${tier2_cut:.2f}")
    else:
        print("✅ No Tier 2 payout or inactive code.")
