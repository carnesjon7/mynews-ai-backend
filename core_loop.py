# Include Hera.Billing logic
from agents.hera_billing import run_billing_cycle

def run_all_agents():
    run_billing_cycle()
    # Call other agent routines as needed

if __name__ == "__main__":
    run_all_agents()
