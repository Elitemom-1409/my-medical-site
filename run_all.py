import sys
import os

# This tells Python to look in our folders for the logic
sys.path.append(os.getcwd())

try:
    from core.pipeline.orchestrator import MasterOrchestrator
    from data.expander import GlossaryExpander
    import random

    print("🤖 ENGINE ACTIVATED: Starting production cycle...")
    
    # 1. Load the medical data
    expander = GlossaryExpander([])
    nodes = expander.expand()
    
    if nodes:
        # 2. Pick a random disease and run the factory
        target = random.choice(nodes)
        orch = MasterOrchestrator()
        orch.run_automation_cycle(target)
        print("✅ SUCCESS: New article produced!")
    else:
        print("❌ ERROR: No medical data found to process.")

except Exception as e:
    print(f"❌ FATAL ERROR during production: {e}")
    sys.exit(1)
