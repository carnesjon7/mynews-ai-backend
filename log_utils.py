# Logs all critical actions for audit trail
def log_action(agent_name, action, metadata=None):
    print(f"[LOG] {agent_name}: {action} | Meta: {metadata}")
