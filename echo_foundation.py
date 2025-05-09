# Echo.Foundation: Captures and preserves the founder's digital essence
from utils.legacy_utils import log_decision, store_voice_sample

def preserve_legacy(event):
    log_decision(event)
    store_voice_sample(event)
