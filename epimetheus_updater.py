# Epimetheus.Updater: Keeps all agents updated with the latest tech and standards
from utils.update_utils import scan_codebase, fetch_updates, apply_patch, notify_zeus

def run_update_cycle():
    outdated = scan_codebase()
    for agent in outdated:
        update_info = fetch_updates(agent)
        if update_info['approved']:
            apply_patch(agent, update_info)
        else:
            notify_zeus(agent, update_info)
