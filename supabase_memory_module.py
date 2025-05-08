
from supabase import create_client, Client
from datetime import datetime
import os

SUPABASE_URL = "https://ifhorseomgyzdabhexwg.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlmaG9yc2VvbWd5emRhYmhleHdnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY3MTI1NzcsImV4cCI6MjA2MjI4ODU3N30.LrYYFn3jknsMfsiv7qtzksf-3aQqpEvGoF8vt0krbXs"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def save_memory(user_id: str, app_name: str, memory_data: dict):
    """Upserts memory data for a specific user and app."""
    response = supabase.table("user_memory").upsert({
        "user_id": user_id,
        "app_name": app_name,
        "memory_data": memory_data,
        "updated_at": datetime.utcnow().isoformat()
    }).execute()
    return response

def get_memory(user_id: str, app_name: str):
    """Retrieves memory data for a specific user and app."""
    response = supabase.table("user_memory") \
        .select("memory_data") \
        .eq("user_id", user_id) \
        .eq("app_name", app_name) \
        .limit(1).execute()
    
    if response.data and len(response.data) > 0:
        return response.data[0]["memory_data"]
    return None
