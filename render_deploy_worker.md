
# Render Deployment Instructions for Agent Scheduler

## To Deploy As Background Worker

1. Go to your [Render Dashboard](https://dashboard.render.com).
2. Click "New +" > Background Worker.
3. Choose your repo (must include `scheduler.py` and `core_loop.py`)
4. Use the following settings:

- **Name:** agent-scheduler
- **Environment:** Python
- **Start Command:** `python scheduler.py`
- **Instance Type:** Starter or above
- **Environment Variables:** match your .env

## To Run Manually from Web Service

Alternatively, deploy as a standard web service and use:

- **Start Command:** `python core_loop.py`
