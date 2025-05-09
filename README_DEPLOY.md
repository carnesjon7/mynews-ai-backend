
# AI Reformation Agent Stack – Launch Instructions

## Setup Steps

1. Upload all files in this bundle to your GitHub repo.
2. Set environment variables in `.env` or Render.
3. Import `supabase_schema.sql` into your Supabase SQL editor.
4. Deploy `scheduler.py` as a background worker OR run `core_loop.py` manually.
5. Add agent triggers in `scheduler.py` as needed.

## Optional:
- Monitor agent activity using the `agent_logs` table.
- Add more agents by dropping their `.py` into the agents folder and registering them in `core_loop.py`.

You now have a fully autonomous AI agent stack running a multi-niche, high-ROI marketing system. Launch wisely.
