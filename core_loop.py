# Connects and triggers all agents in sequence
from dotenv import load_dotenv
import os

from agents.hermes_comment_strike import run_comment_task
from agents.thalia_ghostwriter import generate_affiliate_emails
from agents.clio_minor_fixer import report_site_issues
from agents.apollo_splitcopy import run_split_test
from agents.athena_roi import analyze_affiliate_roi
from agents.hephaestus_bundleops import generate_bundles
from agents.hermes_contentforge import repurpose_content
from agents.iris_cartwhisper import recover_abandoned_carts
from agents.hera_thankyou import send_thank_you_notes
from agents.athena_viraltuner import tune_viral_assets

load_dotenv()

def run_all_agents():
    run_comment_task()
    generate_affiliate_emails()
    report_site_issues()
    run_split_test()
    analyze_affiliate_roi()
    generate_bundles()
    repurpose_content()
    recover_abandoned_carts()
    send_thank_you_notes()
    tune_viral_assets()

if __name__ == "__main__":
    run_all_agents()
