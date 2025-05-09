-- Add billing log
create table if not exists billing_log (
  id uuid primary key default uuid_generate_v4(),
  name text,
  amount numeric,
  status text,
  critical boolean,
  action_by text,
  created_at timestamp default timezone('utc'::text, now())
);
