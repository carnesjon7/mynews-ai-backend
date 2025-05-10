
# ZEUS CORE LOOP TRIGGER – SIMPLE STARTUP PATCH

# This file ensures the Zeus backend activates automatically when deployed.
# Drop this in your backend directory and make sure it's referenced in your main app.

import time

def run():
    print("⚡ Zeus Core Loop Activated...")
    while True:
        # Simulate heartbeat
        print("🧠 Zeus is scanning for directives...")
        # Here Zeus would scan GitHub, check .env, and begin agent routines
        time.sleep(600)  # Check every 10 minutes

# Automatically start if run directly
if __name__ == "__main__":
    run()
