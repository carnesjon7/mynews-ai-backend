-- Agent logs, threat logs, innovation alerts, and snapshots
create table if not exists agent_logs (
  id uuid primary key default uuid_generate_v4(),
  agent_name text,
  action text,
  metadata jsonb,
  created_at timestamp default timezone('utc'::text, now())
);

create table if not exists threat_logs (
  id uuid primary key default uuid_generate_v4(),
  source_ip text,
  description text,
  level text,
  created_at timestamp default timezone('utc'::text, now())
);

create table if not exists innovation_alerts (
  id uuid primary key default uuid_generate_v4(),
  source text,
  title text,
  summary text,
  created_at timestamp default timezone('utc'::text, now())
);
