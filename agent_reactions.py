async def handle_affiliate_activated(data):
    print("Affiliate Activated:", data["data"]["attributes"]["customer_email"])

async def handle_subscription_created(data):
    print("Subscription Created:", data["data"]["attributes"]["customer_email"])
