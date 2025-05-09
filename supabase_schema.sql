-- Extend logging infrastructure
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
