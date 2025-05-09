# Hera.Billing: Monitors and pays subscriptions, escalates to Zeus for critical approvals
import os
from dotenv import load_dotenv
from utils.billing_utils import get_due_bills, pay_bill, notify_zeus

load_dotenv()

def run_billing_cycle():
    bills = get_due_bills()
    for bill in bills:
        if bill['critical']:
            decision = notify_zeus(bill)
            if decision != 'approved':
                print(f"Billing for {bill['name']} requires Zeus approval: {decision}")
                continue
        pay_bill(bill)
