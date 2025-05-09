# Erebus.Wraith 72-Hour Capital Injection Protocol
from utils.erebus_ops import run_72h_ops, terminate_ops

def initiate_72h_capital_injection():
    print("💸 Erebus.Wraith Capital Injection (72-Hour Mode) ACTIVATED")
    run_72h_ops()
    print("🧭 Countdown started: Erebus will self-terminate after 72 hours.")
    terminate_ops()
