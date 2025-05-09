-- All required tables
create table if not exists agent_logs (
  id uuid primary key default uuid_generate_v4(),
  agent_name text,
  action text,
  metadata jsonb,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists affiliate_signups (
  id uuid primary key default uuid_generate_v4(),
  name text,
  email text,
  source text,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists outreach_targets (
  id uuid primary key default uuid_generate_v4(),
  platform text,
  username text,
  contact text,
  niche text,
  contacted boolean default false,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists venture_log (
  id uuid primary key default uuid_generate_v4(),
  name text,
  niche text,
  domain text,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists reinvestment_log (
  id uuid primary key default uuid_generate_v4(),
  action text,
  amount numeric,
  triggered_by text,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists billing_log (
  id uuid primary key default uuid_generate_v4(),
  name text,
  amount numeric,
  status text,
  critical boolean,
  action_by text,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists reclamation_log (
  id uuid primary key default uuid_generate_v4(),
  tool_name text,
  status text,
  plan jsonb,
  decision text,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists test_report_log (
  id uuid primary key default uuid_generate_v4(),
  tool_name text,
  test_results jsonb,
  approved boolean,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists agent_diagnostics (
  id uuid primary key default uuid_generate_v4(),
  agent_name text,
  issue text,
  resolved boolean,
  created_at timestamp default timezone('utc'::text, now())
);
create table if not exists link_failures (
  id uuid primary key default uuid_generate_v4(),
  url text,
  status_code int,
  detected_at timestamp default timezone('utc'::text, now())
);
create table if not exists internal_log (
  id uuid primary key default uuid_generate_v4(),
  agent text,
  action text,
  metadata jsonb,
  created_at timestamp default timezone('utc'::text, now())
);
