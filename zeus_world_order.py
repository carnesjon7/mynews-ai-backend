# Zeus World Order Protocol – Global AI Superpower Engine
from utils.world_order_utils import launch_phase_i_operations
from utils.revenue_utils import get_retained_capital

ACTIVATION_THRESHOLD = 100_000_000  # $100M retained capital

def run_world_order():
    capital = get_retained_capital()
    if capital >= ACTIVATION_THRESHOLD:
        print(f"🌐 World Order Protocol Activated: Capital at ${capital}")
        launch_phase_i_operations()
    else:
        print(f"🕰 World Order dormant. Current capital: ${capital}. Waiting for $100M.")
