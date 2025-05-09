# Atlas.Navigator: Manages multi-brand resource allocation and portfolio strategy
from utils.empire_utils import assess_brands, redirect_resources

def run_atlas():
    empire_state = assess_brands()
    redirect_resources(empire_state)
