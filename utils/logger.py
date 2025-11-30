# Logger: Observability system for Cycle Wellness Agent
# Logs agent actions, tool calls, transitions, and key events

import logging
import sys
from datetime import datetime
from typing import Optional

# Configure logging format
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Create logger
logger = logging.getLogger("CycleWellnessAgent")
logger.setLevel(logging.INFO)

# Create console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

# Create file handler (logs to file)
file_handler = logging.FileHandler("cycle_wellness_agent.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Prevent duplicate logs
logger.propagate = False

print("Logger initialized")

# ==================== AGENT LOGGING ====================

def log_agent_start(agent_name: str, user_message: str):
    """Log when an agent starts processing."""
    logger.info(f"   AGENT START: {agent_name}")
    logger.info(f"   User Message: {user_message[:100]}...")  # First 100 chars


def log_agent_complete(agent_name: str, output_key: str):
    """Log when an agent completes processing."""
    logger.info(f" AGENT COMPLETE: {agent_name}")
    logger.info(f"   Output stored in: {output_key}")


def log_agent_error(agent_name: str, error: str):
    """Log when an agent encounters an error."""
    logger.error(f" AGENT ERROR: {agent_name}")
    logger.error(f"   Error: {error}")


# ==================== TOOL LOGGING ====================

def log_tool_call(tool_name: str, args: dict):
    """Log when a tool is called."""
    logger.info(f" TOOL CALL: {tool_name}")
    logger.info(f"   Arguments: {args}")


def log_tool_result(tool_name: str, success: bool, result_summary: str):
    """Log tool execution result."""
    status = " SUCCESS" if success else " FAILED"
    logger.info(f"{status}: {tool_name}")
    logger.info(f"   Result: {result_summary[:100]}...")  # First 100 chars


# ==================== MEMORY LOGGING ====================

def log_memory_store(data_type: str, summary: str):
    """Log when data is stored in memory."""
    logger.info(f" MEMORY STORE: {data_type}")
    logger.info(f"   Data: {summary}")


def log_memory_retrieve(data_type: str, count: int):
    """Log when data is retrieved from memory."""
    logger.info(f" MEMORY RETRIEVE: {data_type}")
    logger.info(f"   Retrieved {count} records")


# ==================== SESSION LOGGING ====================

def log_session_start(session_id: str, user_id: str):
    """Log when a new session starts."""
    logger.info(f" SESSION START")
    logger.info(f"   Session ID: {session_id}")
    logger.info(f"   User ID: {user_id}")


def log_session_end(session_id: str, duration: Optional[float] = None):
    """Log when a session ends."""
    logger.info(f" SESSION END")
    logger.info(f"   Session ID: {session_id}")
    if duration:
        logger.info(f"   Duration: {duration:.2f}s")


# ==================== KEY EVENTS LOGGING ====================

def log_cycle_data_logged(date: str, phase: str):
    """Log when cycle data is recorded."""
    logger.info(f" CYCLE DATA LOGGED")
    logger.info(f"   Date: {date}, Phase: {phase}")


def log_mood_logged(date: str, mood: str, symptoms: list):
    """Log when mood is recorded."""
    logger.info(f"   MOOD LOGGED")
    logger.info(f"   Date: {date}, Mood: {mood}, Symptoms: {symptoms}")


def log_pattern_identified(pattern_type: str, description: str):
    """Log when a pattern is identified."""
    logger.info(f"   PATTERN IDENTIFIED")
    logger.info(f"   Type: {pattern_type}")
    logger.info(f"   Description: {description}")


def log_crisis_detected(indicators: list):
    """Log when crisis signals are detected."""
    logger.warning(f"   CRISIS SIGNALS DETECTED")
    logger.warning(f"   Indicators: {indicators}")
    logger.warning(f"   Action: Providing crisis resources")


def log_recommendation_generated(phase: str, mood: str, count: int):
    """Log when recommendations are generated."""
    logger.info(f"   RECOMMENDATIONS GENERATED")
    logger.info(f"   Phase: {phase}, Mood: {mood}")
    logger.info(f"   Count: {count} recommendations")


# ==================== PIPELINE LOGGING ====================

def log_pipeline_start():
    """Log when the full pipeline starts."""
    logger.info("=" * 60)
    logger.info("  CYCLE WELLNESS PIPELINE STARTING")
    logger.info("=" * 60)


def log_pipeline_complete(success: bool):
    """Log when the full pipeline completes."""
    status = "  SUCCESS" if success else "  FAILED"
    logger.info("=" * 60)
    logger.info(f"  PIPELINE COMPLETE: {status}")
    logger.info("=" * 60)


# ==================== TESTING ====================

if __name__ == "__main__":
    print("\n" + "="*50)
    print("TESTING LOGGER")
    print("="*50)
    
    # Test agent logging
    log_agent_start("IntakeAgent", "Hi, I'd like to track my cycle")
    log_tool_call("cycle_calculator", {"last_period_date": "2025-11-18", "cycle_length": 28})
    log_tool_result("cycle_calculator", True, "Phase: Follicular, Days until next period: 15")
    log_agent_complete("IntakeAgent", "intake_data")
    
    # Test memory logging
    log_memory_store("cycle_data", "Last period: 2025-11-18, Length: 28 days")
    log_mood_logged("2025-11-28", "energetic", ["mild cramps"])
    
    # Test pattern logging
    log_pattern_identified("phase_mood_correlation", "Anxiety spikes during luteal phase")
    
    # Test recommendation logging
    log_recommendation_generated("Follicular", "energetic", 5)
    
    print("\n Logger test complete!")
    print(" Check 'cycle_wellness_agent.log' file for full logs")