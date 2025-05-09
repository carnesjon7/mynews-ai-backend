# Final core loop scheduler with daily and adaptive run options
import schedule
import time
from core_loop import run_all_agents

def schedule_agents():
    schedule.every().day.at("03:00").do(run_all_agents)  # Daily master run
    schedule.every(6).hours.do(run_all_agents)           # Adaptive interval

    print("📅 Agent scheduler active...")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_agents()
