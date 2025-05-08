from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

@app.route("/", methods=["GET"])
def index():
    return "MyNews.AI backend is running."

@app.route("/memory", methods=["POST"])
def update_memory():
    data = request.json
    user_id = data.get("user_id")
    app_name = data.get("app_name")
    memory_data = data.get("memory_data")

    if not user_id or not app_name:
        return jsonify({"error": "Missing user_id or app_name"}), 400

    # Try to upsert into the user_memory table
    try:
        response = supabase.table("user_memory").upsert({
            "user_id": user_id,
            "app_name": app_name,
            "memory_data": memory_data
        }, on_conflict=["user_id", "app_name"]).execute()
        return jsonify({"message": "Memory updated", "data": response.data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/memory", methods=["GET"])
def get_memory():
    user_id = request.args.get("user_id")
    app_name = request.args.get("app_name")

    if not user_id or not app_name:
        return jsonify({"error": "Missing user_id or app_name"}), 400

    try:
        response = supabase.table("user_memory").select("*").eq("user_id", user_id).eq("app_name", app_name).execute()
        if response.data:
            return jsonify({"memory_data": response.data[0]["memory_data"]}), 200
        else:
            return jsonify({"memory_data": None}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
