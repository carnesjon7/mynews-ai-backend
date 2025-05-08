
from fastapi import APIRouter, Request
from hermes_billing_agent import handle_payment_success, handle_subscription_created
from clio_tracker_agent import handle_affiliate_activated, handle_subscription_cancelled

router = APIRouter()

@router.post("/webhooks/lemon")
async def lemon_webhook(request: Request):
    payload = await request.json()
    event = payload.get("meta", {}).get("event_name")

    if event == "subscription_payment_success":
        handle_payment_success(payload)
    elif event == "subscription_created":
        handle_subscription_created(payload)
    elif event == "affiliate_activated":
        handle_affiliate_activated(payload)
    elif event == "subscription_cancelled":
        handle_subscription_cancelled(payload)
    else:
        print("[Router] Unhandled event:", event)

    return {"status": "received"}
