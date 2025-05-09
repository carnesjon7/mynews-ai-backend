# Schedules full agent stack + weekly Zeus.Reporter
import schedule
import time
from core_loop import run_all_agents
from agents.zeus_reporter import run_weekly_report

def schedule_agents():
    schedule.every().day.at("03:00").do(run_all_agents)
    schedule.every(6).hours.do(run_all_agents)
    schedule.every().sunday.at("08:00").do(run_weekly_report)

    print("📅 Full-stack scheduler running...")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_agents()
