# Unified data read/write handler for Supabase
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def log_event(table: str, data: dict):
    client = get_supabase_client()
    response = client.table(table).insert(data).execute()
    return response
