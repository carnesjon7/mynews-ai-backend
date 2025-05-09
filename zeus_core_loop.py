# Final Zeus Core Loop
from zeus_overseer import run as run_zeus
from boot_manager import start as boot_start

def launch_empire():
    boot_start()
    run_zeus()

if __name__ == "__main__":
    launch_empire()
