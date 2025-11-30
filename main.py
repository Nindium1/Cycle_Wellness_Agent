# main.py - Cycle Wellness Agent Main Application
import os
import sys
from setup import SequentialAgent, InMemoryRunner

# Import all three agents
from agents.intake_agent import intake_agent
from agents.analysis_agent import analysis_agent
from agents.wellness_agent import wellness_agent

from utils.logger import (
    log_pipeline_start, 
    log_pipeline_complete,
    log_agent_start,
    log_agent_complete
)

# Create the Sequential Agent (root agent) that chains all 3 agents
root_agent = SequentialAgent(
    name="CycleWellnessPipeline",
    sub_agents=[intake_agent, analysis_agent, wellness_agent],
)

print("✅ Sequential Agent created.")

# Create the runner
runner = InMemoryRunner(agent=root_agent)

print("✅ Runner created.")

# Test the complete pipeline
async def test_pipeline():
    """Test the complete 3-agent pipeline"""
    print("\n" + "="*50)
    print("TESTING CYCLE WELLNESS AGENT PIPELINE")
    print("="*50 + "\n")
    
     # Log pipeline start
    log_pipeline_start()

    user_message = "Hi, I'd like to track my cycle and mood. My last period started on 2025-11-18. My average cycle length is 28 days.Right now I'm feeling anxious and tired."
    print(f"User: {user_message}\n")
    
    # Log agent start
    log_agent_start("CycleWellnessPipeline", user_message)

    try:
        response = await runner.run_debug(user_message)

        # Log successful completion
        log_agent_complete("CycleWellnessPipeline", "final_response")
        log_pipeline_complete(success=True)
        
        print(f"\n Agent Response:\n{response}\n")
        print("="*50)
        print(" Pipeline test PASSED!")
        print("="*50)
        print("\n Check 'cycle_wellness_agent.log' for detailed logs")

    except Exception as e:
        log_pipeline_complete(success=False)
        print(f" ERROR: {e}")
        import traceback
        traceback.print_exc()

# Run the test
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_pipeline())