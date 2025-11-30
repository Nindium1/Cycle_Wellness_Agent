# Pattern Analyzer Tool: Analyzes mood and symptom patterns over time

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from setup import FunctionTool

def analyze_mood_patterns(mood_logs: str) -> dict:
    """
    Analyzes mood and symptom patterns from historical data.
    
    Args:
        mood_logs: JSON string containing mood log entries. Each entry should have:
                   - date: str (YYYY-MM-DD)
                   - cycle_phase: str (Menstrual, Follicular, Ovulation, Luteal)
                   - mood: str (happy, anxious, sad, irritable, energetic, tired, etc.)
                   - symptoms: list (physical symptoms)
                   - notes: str (optional user notes)
    
    Returns:
        Dictionary with pattern analysis, correlations, and insights
    """
    try:
        import json
        
        # Parse the JSON string to list
        if isinstance(mood_logs, str):
            mood_logs = json.loads(mood_logs)
        elif not isinstance(mood_logs, list):
            mood_logs = []
        if not mood_logs or len(mood_logs) == 0:
            return {
                "status": "no_data",
                "message": "No mood data available yet. Keep logging to see patterns!",
                "patterns_found": []
            }
        
        # Initialize pattern tracking
        phase_mood_map = {
            "Menstrual": [],
            "Follicular": [],
            "Ovulation": [],
            "Luteal": []
        }
        
        all_moods = []
        symptom_frequency = {}
        
        # Process each mood log
        for log in mood_logs:
            phase = log.get("cycle_phase", "Unknown")
            mood = log.get("mood", "").lower()
            symptoms = log.get("symptoms", [])
            
            # Track moods by phase
            if phase in phase_mood_map and mood:
                phase_mood_map[phase].append(mood)
            
            # Track all moods
            if mood:
                all_moods.append(mood)
            
            # Track symptom frequency
            for symptom in symptoms:
                symptom_frequency[symptom] = symptom_frequency.get(symptom, 0) + 1
        
        # Analyze patterns
        patterns = []
        
        # Pattern 1: Most common mood by phase
        for phase, moods in phase_mood_map.items():
            if moods:
                most_common = max(set(moods), key=moods.count)
                frequency = moods.count(most_common)
                if frequency > 1:  # Only report if pattern appears more than once
                    patterns.append({
                        "type": "phase_mood_correlation",
                        "phase": phase,
                        "mood": most_common,
                        "frequency": frequency,
                        "insight": f"You tend to feel {most_common} during your {phase} phase."
                    })
        
        # Pattern 2: Most common symptoms
        if symptom_frequency:
            top_symptoms = sorted(symptom_frequency.items(), key=lambda x: x[1], reverse=True)[:3]
            for symptom, count in top_symptoms:
                if count > 1:
                    patterns.append({
                        "type": "symptom_pattern",
                        "symptom": symptom,
                        "frequency": count,
                        "insight": f"{symptom.capitalize()} appears frequently in your logs ({count} times)."
                    })
        
        # Pattern 3: Overall mood trend
        if all_moods:
            negative_moods = ["anxious", "sad", "irritable", "depressed", "angry", "overwhelmed"]
            positive_moods = ["happy", "energetic", "calm", "content", "peaceful"]
            
            negative_count = sum(1 for mood in all_moods if mood in negative_moods)
            positive_count = sum(1 for mood in all_moods if mood in positive_moods)
            
            if negative_count > positive_count * 1.5:  # Significantly more negative
                patterns.append({
                    "type": "overall_trend",
                    "trend": "predominantly_negative",
                    "insight": "Your logs show more challenging moods. Consider discussing with a healthcare provider."
                })
            elif positive_count > negative_count * 1.5:  # Significantly more positive
                patterns.append({
                    "type": "overall_trend",
                    "trend": "predominantly_positive",
                    "insight": "Your mood logs show many positive moments! Keep up the self-care."
                })
        
        return {
            "status": "success",
            "total_logs_analyzed": len(mood_logs),
            "patterns_found": patterns,
            "summary": f"Analyzed {len(mood_logs)} mood logs and found {len(patterns)} patterns."
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error analyzing patterns: {str(e)}",
            "patterns_found": []
        }

# Test the function directly 
print("✅ Pattern analyzer function created")

# Sample test data 
import json
test_logs = json.dumps([
    {"date": "2025-11-10", "cycle_phase": "Luteal", "mood": "anxious", "symptoms": ["cramps", "fatigue"]},
    {"date": "2025-11-15", "cycle_phase": "Luteal", "mood": "irritable", "symptoms": ["headache", "fatigue"]},
    {"date": "2025-11-20", "cycle_phase": "Menstrual", "mood": "tired", "symptoms": ["cramps"]},
    {"date": "2025-11-25", "cycle_phase": "Follicular", "mood": "energetic", "symptoms": []},
])

print(f" Test with {len(test_logs)} logs:")
result = analyze_mood_patterns(test_logs)
print(f"   Status: {result['status']}")
print(f"   Patterns found: {len(result['patterns_found'])}")
if result['patterns_found']:
    print(f"   Sample insight: {result['patterns_found'][0]['insight']}")

# Create the FunctionTool
pattern_analyzer_tool = FunctionTool(
    func=analyze_mood_patterns
)

print("✅ pattern_analyzer_tool wrapped as FunctionTool")