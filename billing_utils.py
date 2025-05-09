# Billing utilities for Hera
def get_due_bills():
    # Placeholder function; this would interface with Supabase or a billing API
    return [
        {"name": "Render Starter", "amount": 7, "due": "2025-05-10", "critical": True},
        {"name": "Beehiiv", "amount": 39, "due": "2025-05-12", "critical": False}
    ]

def pay_bill(bill):
    # Simulated bill payment
    print(f"Paid {bill['name']} - ${bill['amount']}")

def notify_zeus(bill):
    # Simulate Zeus.Overseer approval workflow
    print(f"Requesting approval from Zeus for {bill['name']}...")
    return 'approved'
