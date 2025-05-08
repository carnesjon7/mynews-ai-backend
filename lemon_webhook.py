from fastapi import APIRouter, Request
from agent_reactions import handle_affiliate_activated, handle_subscription_created

router = APIRouter(prefix="/webhooks/lemon")

@router.post("")
async def lemon_webhook_handler(request: Request):
    payload = await request.json()
    event_name = payload.get("meta", {}).get("event_name")

    if event_name == "affiliate_activated":
        await handle_affiliate_activated(payload)
    elif event_name == "subscription_created":
        await handle_subscription_created(payload)

    return {"status": "received"}
from fastapi import FastAPI
app = FastAPI()
app.include_router(router)
