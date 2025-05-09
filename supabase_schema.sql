
-- Supabase table schemas for AI Reformation agent logging
create table if not exists agent_logs (
  id uuid primary key default uuid_generate_v4(),
  agent_name text not null,
  action text not null,
  metadata jsonb,
  created_at timestamp with time zone default timezone('utc'::text, now())
);

create table if not exists affiliate_signups (
  id uuid primary key default uuid_generate_v4(),
  name text,
  email text,
  source text,
  created_at timestamp with time zone default timezone('utc'::text, now())
);

create table if not exists outreach_targets (
  id uuid primary key default uuid_generate_v4(),
  platform text,
  username text,
  contact text,
  niche text,
  contacted boolean default false,
  created_at timestamp with time zone default timezone('utc'::text, now())
);
