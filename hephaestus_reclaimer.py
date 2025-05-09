# Hephaestus.Reclaimer: SaaS independence and sovereignty agent
from utils.reclamation_utils import evaluate_dependency, deploy_self_hosted_alt, notify_zeus
from utils.revenue_utils import get_monthly_revenue

DEPENDENCIES = [
    {"name": "Render", "type": "hosting", "threshold": 25000},
    {"name": "Framer", "type": "frontend", "threshold": 25000},
    {"name": "Beehiiv", "type": "email", "threshold": 20000},
    {"name": "Stripe", "type": "billing", "threshold": 30000},
    {"name": "OpenAI", "type": "AI", "threshold": 50000},
    {"name": "ElevenLabs", "type": "voice", "threshold": 40000}
]

def run_reclaimer():
    revenue = get_monthly_revenue()
    for dep in DEPENDENCIES:
        if revenue >= dep["threshold"] and evaluate_dependency(dep["name"]):
            deploy_self_hosted_alt(dep["name"])
            notify_zeus(dep["name"], revenue)
        else:
            print(f"⏳ {dep['name']} still optimal or below threshold.")
