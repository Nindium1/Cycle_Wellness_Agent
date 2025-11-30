# Memory Management: Cycle Wellness Agent Memory System
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.genai import types

# Try to import load_memory, but don't fail if it's not available
try:
    from google.adk.memory import load_memory
    print("✅ load_memory tool imported")
except ImportError:
    load_memory = None
    print(" load_memory not available in this ADK version (optional)")
from datetime import datetime
from typing import List, Dict, Optional

# Define constants
APP_NAME = "CycleWellnessApp"
USER_ID = "cycle_user"

# Create Session Service (handles conversations)
session_service = InMemorySessionService()
print("✅ InMemorySessionService created")

# Create Memory Service (stores long-term memories)
memory_service = InMemoryMemoryService()
print("✅ InMemoryMemoryService created")

# In-memory storage for structured cycle data
cycle_data_store = {
    "cycle_info": {},      # Current cycle information
    "mood_logs": [],       # List of all mood logs
    "patterns": [],        # Identified patterns
    "user_preferences": {} # User preferences
}

print("✅ Cycle data store initialized")


# ====== SESSION MANAGEMENT ======

async def run_session(runner_instance, user_queries, session_id: str = "default"):
    """
    Helper function to run queries in a session and display responses.
    Follows Kaggle pattern.
    """
    print(f"\n### Session: {session_id}")
    
    # Create or retrieve session
    try:
        session = await session_service.create_session(
            app_name=APP_NAME, user_id=USER_ID, session_id=session_id
        )
    except:
        session = await session_service.get_session(
            app_name=APP_NAME, user_id=USER_ID, session_id=session_id
        )
    
    # Convert single query to list
    if isinstance(user_queries, str):
        user_queries = [user_queries]
    
    # Process each query
    for query in user_queries:
        print(f"\n User > {query}")
        query_content = types.Content(role="user", parts=[types.Part(text=query)])
        
        # Stream agent response
        async for event in runner_instance.run_async(
            user_id=USER_ID, session_id=session.id, new_message=query_content
        ):
            if event.is_final_response() and event.content and event.content.parts:
                text = event.content.parts[0].text
                if text and text != "None":
                    print(f" Agent > {text}")


async def save_session_to_memory(session_id: str):
    """Save a session to long-term memory (Kaggle pattern)."""
    try:
        session = await session_service.get_session(
            app_name=APP_NAME, user_id=USER_ID, session_id=session_id
        )
        await memory_service.add_session_to_memory(session)
        print(f"✅ Session '{session_id}' saved to memory!")
        return True
    except Exception as e:
        print(f" Error saving session: {e}")
        return False


# ====== CYCLE DATA MANAGEMENT ======

def store_cycle_info(last_period_date: str, cycle_length: int, user_id: str = USER_ID) -> bool:
    """
    Store current cycle information.
    
    Args:
        last_period_date: Date in format 'YYYY-MM-DD'
        cycle_length: Average cycle length in days
        user_id: User identifier
    """
    try:
        cycle_data_store["cycle_info"][user_id] = {
            "last_period_date": last_period_date,
            "cycle_length": cycle_length,
            "updated_at": datetime.now().isoformat()
        }
        print(f"✅ Cycle info stored: Last period {last_period_date}, Length {cycle_length} days")
        return True
    except Exception as e:
        print(f" Error storing cycle info: {e}")
        return False


def get_cycle_info(user_id: str = USER_ID) -> Optional[Dict]:
    """Retrieve current cycle information."""
    return cycle_data_store["cycle_info"].get(user_id)


def add_mood_log(date: str, cycle_phase: str, mood: str, symptoms: List[str], 
                 notes: str = "", user_id: str = USER_ID) -> bool:
    """
    Add a mood log entry.
    
    Args:
        date: Date in format 'YYYY-MM-DD'
        cycle_phase: Current cycle phase (Menstrual, Follicular, Ovulation, Luteal)
        mood: Current mood state
        symptoms: List of symptoms
        notes: Optional user notes
        user_id: User identifier
    """
    try:
        mood_entry = {
            "user_id": user_id,
            "date": date,
            "cycle_phase": cycle_phase,
            "mood": mood,
            "symptoms": symptoms,
            "notes": notes,
            "logged_at": datetime.now().isoformat()
        }
        cycle_data_store["mood_logs"].append(mood_entry)
        print(f"✅ Mood log added: {date} - {mood} ({cycle_phase} phase)")
        return True
    except Exception as e:
        print(f" Error adding mood log: {e}")
        return False


def get_mood_logs(user_id: str = USER_ID, limit: int = 30, 
                  cycle_phase: Optional[str] = None) -> List[Dict]:
    """
    Retrieve mood logs with optional filtering.
    
    Args:
        user_id: User identifier
        limit: Maximum number of logs to return
        cycle_phase: Optional filter by cycle phase
    
    Returns:
        List of mood log entries
    """
    logs = [log for log in cycle_data_store["mood_logs"] if log["user_id"] == user_id]
    
    # Filter by phase if specified
    if cycle_phase:
        logs = [log for log in logs if log["cycle_phase"].lower() == cycle_phase.lower()]
    
    # Sort by date (most recent first) and limit
    logs = sorted(logs, key=lambda x: x["date"], reverse=True)[:limit]
    
    print(f"✅ Retrieved {len(logs)} mood logs" + (f" for {cycle_phase} phase" if cycle_phase else ""))
    return logs


def store_pattern(pattern_type: str, description: str, data: Dict, 
                  user_id: str = USER_ID) -> bool:
    """
    Store identified patterns and insights.
    
    Args:
        pattern_type: Type of pattern (e.g., 'phase_mood_correlation', 'symptom_pattern')
        description: Human-readable description
        data: Additional pattern data
        user_id: User identifier
    """
    try:
        pattern_entry = {
            "user_id": user_id,
            "type": pattern_type,
            "description": description,
            "data": data,
            "identified_at": datetime.now().isoformat()
        }
        cycle_data_store["patterns"].append(pattern_entry)
        print(f"✅ Pattern stored: {pattern_type}")
        return True
    except Exception as e:
        print(f" Error storing pattern: {e}")
        return False


def get_patterns(user_id: str = USER_ID, pattern_type: Optional[str] = None) -> List[Dict]:
    """
    Retrieve stored patterns with optional type filtering.
    
    Args:
        user_id: User identifier
        pattern_type: Optional filter by pattern type
    
    Returns:
        List of pattern entries
    """
    patterns = [p for p in cycle_data_store["patterns"] if p["user_id"] == user_id]
    
    if pattern_type:
        patterns = [p for p in patterns if p["type"] == pattern_type]
    
    print(f"✅ Retrieved {len(patterns)} patterns")
    return patterns


def clear_all_data(user_id: str = USER_ID):
    """Clear all stored data for a user (useful for testing)."""
    if user_id in cycle_data_store["cycle_info"]:
        del cycle_data_store["cycle_info"][user_id]
    
    cycle_data_store["mood_logs"] = [log for log in cycle_data_store["mood_logs"] 
                                      if log["user_id"] != user_id]
    cycle_data_store["patterns"] = [p for p in cycle_data_store["patterns"] 
                                     if p["user_id"] != user_id]
    
    print(f"✅ All data cleared for user {user_id}")


# ====== TESTING ======

print("\n" + "="*50)
print("TESTING MEMORY SYSTEM")
print("="*50)

# Test 1: Store cycle info
print("\n Test 1: Storing cycle information...")
store_cycle_info("2025-11-18", 28)

# Test 2: Retrieve cycle info
print("\n Test 2: Retrieving cycle information...")
cycle_info = get_cycle_info()
print(f"   Retrieved: {cycle_info}")

# Test 3: Add mood logs
print("\n Test 3: Adding mood logs...")
add_mood_log("2025-11-20", "Follicular", "energetic", [], "Feeling great!")
add_mood_log("2025-11-25", "Ovulation", "happy", ["mild cramps"], "Productive day")
add_mood_log("2025-11-28", "Luteal", "anxious", ["fatigue", "headache"], "Feeling stressed")

# Test 4: Retrieve all mood logs
print("\n Test 4: Retrieving all mood logs...")
all_logs = get_mood_logs(limit=10)
print(f"   Total logs: {len(all_logs)}")

# Test 5: Retrieve mood logs by phase
print("\n Test 5: Retrieving Luteal phase logs only...")
luteal_logs = get_mood_logs(cycle_phase="Luteal")
print(f"   Luteal logs: {len(luteal_logs)}")

# Test 6: Store pattern
print("\n Test 6: Storing identified pattern...")
store_pattern(
    pattern_type="phase_mood_correlation",
    description="Anxiety tends to spike during luteal phase",
    data={"phase": "Luteal", "mood": "anxious", "frequency": 3}
)

# Test 7: Retrieve patterns
print("\n Test 7: Retrieving patterns...")
patterns = get_patterns()
print(f"   Patterns found: {len(patterns)}")

print("\n" + "="*50)
print("✅ MEMORY SYSTEM READY FOR USE")
print("="*50)
print("\nAvailable functions:")
print("  • store_cycle_info() - Store cycle data")
print("  • get_cycle_info() - Retrieve cycle data")
print("  • add_mood_log() - Add mood/symptom entry")
print("  • get_mood_logs() - Retrieve mood history")
print("  • store_pattern() - Store identified patterns")
print("  • get_patterns() - Retrieve patterns")
print("  • save_session_to_memory() - Save conversations (Kaggle pattern)")
print("="*50)