# Final Deployment Instructions – AI Reformation

## Step 1: Upload to GitHub
Place the full `/agents`, `/utils`, and core files (`core_loop.py`, `scheduler.py`) into your repo.

## Step 2: Supabase Setup
Run `supabase_schema.sql` from each bundle to initialize all tables.

## Step 3: Render Deployment
- Deploy `scheduler.py` as a background worker
- Set environment variables from `.env.template`

## Step 4: Live Monitoring
Ensure all agents log to Supabase and notify you via Hermes.Email

## Step 5: Operate
Your system will now run, heal, scale, invest, launch, and report—entirely autonomously.
