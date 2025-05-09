# Mnemosyne Zero-Knowledge Memory Agent
from utils.zk_utils import request_memory_block

def retrieve_secure_memory(query_id):
    print(f"🔐 ZK Memory Retrieval initiated for query: {query_id}")
    memory = request_memory_block(query_id)
    print(f"📂 Result: {memory}")
