# Integrated core loop for The AI Reformation
from agents.zeus_overseer import run_zeus
from agents.athena_autopilot import run_athena
from agents.plutus_capital import run_plutus
from agents.hera_billing import run_billing_cycle
from agents.daedalus_venturearchitect import run_venture_creation
from agents.hephaestus_reclaimer import run_reclamation_cycle
from agents.prometheus_diagnostica import run_diagnosis_cycle
from agents.hermes_linkwatch import run_linkwatch
from agents.clio_recorder import record_event

def run_all_agents():
    print("🚀 Running Zeus.Overseer...")
    run_zeus()
    
    print("🧠 Running Athena.Autopilot...")
    run_athena()
    
    print("💰 Running Plutus.Capital...")
    run_plutus()
    
    print("💳 Running Hera.Billing...")
    run_billing_cycle()
    
    print("🏗️ Running Daedalus.VentureArchitect...")
    run_venture_creation()
    
    print("⚙️ Running Hephaestus.Reclaimer...")
    run_reclamation_cycle()
    
    print("🩺 Running Prometheus.Diagnostica...")
    run_diagnosis_cycle()
    
    print("🌐 Running Hermes.LinkWatch...")
    run_linkwatch()
    
    print("📝 Logging run with Clio.Recorder...")
    record_event("core_loop", "run_all_agents")

if __name__ == "__main__":
    run_all_agents()
