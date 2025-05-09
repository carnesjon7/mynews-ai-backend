# Central logging agent for internal decisions
from utils.log_utils import log_action

def record_event(agent_name, action, metadata=None):
    log_action(agent_name, action, metadata)
