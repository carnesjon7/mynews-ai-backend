
from fastapi import APIRouter, Request, Header
from starlette.responses import JSONResponse
from supabase import create_client
import os
import json

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.post("/webhooks/lemon")
async def lemon_webhook(request: Request, x_signature: str = Header(None)):
    payload = await request.json()
    event_type = payload.get("meta", {}).get("event_name")
    user_email = payload.get("data", {}).get("attributes", {}).get("user_email", "unknown")
    
    # Memory log
    supabase.table("user_memory").insert({
        "source": "lemon_webhook",
        "summary": f"Received event: {event_type}",
        "data": json.dumps(payload)
    }).execute()

    # Agent logic trigger
    if event_type == "subscription_created":
        handle_subscription_created(payload)
    elif event_type == "subscription_payment_success":
        handle_payment_success(payload)
    elif event_type == "subscription_payment_failed":
        handle_payment_failure(payload)
    elif event_type == "subscription_cancelled":
        handle_subscription_cancelled(payload)
    elif event_type == "affiliate_activated":
        handle_affiliate_activated(payload)

    return JSONResponse({"status": "received"}, status_code=200)

def handle_subscription_created(payload):
    # Hermes.Billing logic
    print("Hermes.Billing: Granting access")

def handle_payment_success(payload):
    print("Hermes.Billing: Payment confirmed")

def handle_payment_failure(payload):
    print("Clio.Support: Flagging user for follow-up")

def handle_subscription_cancelled(payload):
    print("Hermes.Billing: Removing access")

def handle_affiliate_activated(payload):
    print("Hermes.Billing: Registering affiliate payout trail")
