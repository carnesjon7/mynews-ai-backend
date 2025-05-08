import hmac
import hashlib
import json
from fastapi import APIRouter, Header, Request, HTTPException
from starlette.responses import JSONResponse

router = APIRouter()

LEMON_WEBHOOK_SECRET = "your-lemon-squeezy-webhook-secret"

# Replace with actual agent endpoints or internal function calls
def handle_subscription_created(payload): pass
def handle_payment_success(payload): pass
def handle_affiliate_activated(payload): pass
def log_event(event_type, payload): pass

@router.post("/webhooks/lemon")
async def lemon_webhook(
    request: Request,
    x_signature: str = Header(None)
):
    body_bytes = await request.body()
    computed_signature = hmac.new(
        LEMON_WEBHOOK_SECRET.encode(),
        body_bytes,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(computed_signature, x_signature):
        raise HTTPException(status_code=400, detail="Invalid signature")

    payload = json.loads(body_bytes)
    event = payload.get("meta", {}).get("event_name")
    data = payload.get("data", {})

    # Event Routing
    if event == "subscription_created":
        handle_subscription_created(data)
    elif event == "subscription_payment_success":
        handle_payment_success(data)
    elif event == "affiliate_activated":
        handle_affiliate_activated(data)

    log_event(event, data)
    return JSONResponse(content={"success": True})
