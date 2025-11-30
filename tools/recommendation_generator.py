# Recommendation Generator Tool: Generates personalized wellness recommendations

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from setup import FunctionTool
from typing import List

def generate_recommendations(cycle_phase: str, mood: str, symptoms: List[str] = None) -> dict:
    """
    Generates personalized wellness recommendations based on cycle phase, mood, and symptoms.
    
    Args:
        cycle_phase: Current cycle phase (Menstrual, Follicular, Ovulation, Luteal)
        mood: Current mood state (anxious, sad, tired, energetic, happy, etc.)
        symptoms: List of physical symptoms (optional)
    
    Returns:
        Dictionary with personalized recommendations, self-care tips, and resources
    """
    try:
        if symptoms is None:
            symptoms = []
        
        # Normalize inputs
        phase = cycle_phase.lower()
        mood = mood.lower()
        symptoms = [s.lower() for s in symptoms]
        
        # Phase-specific baseline recommendations
        phase_recommendations = {
            "menstrual": {
                "focus": "Rest and gentle self-care",
                "activities": [
                    "Gentle yoga or stretching",
                    "Warm baths with Epsom salts",
                    "Comfort foods that nourish",
                    "Extra sleep and rest time",
                    "Light walks in nature"
                ],
                "avoid": ["Intense exercise", "Major decisions", "Overcommitting"]
            },
            "follicular": {
                "focus": "Energy building and new beginnings",
                "activities": [
                    "Try new workouts or activities",
                    "Start new projects",
                    "Social activities and connections",
                    "Creative pursuits",
                    "Goal setting and planning"
                ],
                "avoid": ["Overextending yourself", "Ignoring nutrition"]
            },
            "ovulation": {
                "focus": "Peak energy and confidence",
                "activities": [
                    "Important conversations or presentations",
                    "High-intensity workouts",
                    "Networking and social events",
                    "Tackling challenging tasks",
                    "Making important decisions"
                ],
                "avoid": ["Wasting your high-energy window", "Poor sleep habits"]
            },
            "luteal": {
                "focus": "Gentle energy management and self-compassion",
                "activities": [
                    "Moderate exercise (yoga, walking)",
                    "Journaling and self-reflection",
                    "Setting boundaries",
                    "Cozy, comforting activities",
                    "Meal prep for upcoming cycle"
                ],
                "avoid": ["Overcommitting socially", "Harsh self-criticism", "Too much caffeine"]
            }
        }
        
        # Mood-specific recommendations
        mood_recommendations = {
            "anxious": [
                "Practice deep breathing (4-7-8 technique)",
                "Try grounding exercises (5-4-3-2-1 method)",
                "Limit caffeine and sugar",
                "Progressive muscle relaxation",
                "Talk to a trusted friend or therapist"
            ],
            "sad": [
                "Get sunlight exposure (even 10 minutes helps)",
                "Reach out to supportive friends/family",
                "Gentle movement or stretching",
                "Journal your feelings",
                "Consider talking to a mental health professional"
            ],
            "tired": [
                "Prioritize 8+ hours of sleep",
                "Take short power naps (20 min max)",
                "Stay hydrated",
                "Eat iron-rich foods",
                "Reduce screen time before bed"
            ],
            "irritable": [
                "Take breaks when needed",
                "Practice saying 'no' to non-essentials",
                "Express feelings through journaling",
                "Try calming activities (bath, music, nature)",
                "Give yourself permission to rest"
            ],
            "overwhelmed": [
                "Break tasks into tiny steps",
                "Practice one thing at a time",
                "Ask for help when needed",
                "Set firm boundaries",
                "Remember: this phase will pass"
            ]
        }
        
        # Symptom-specific recommendations
        symptom_recommendations = {
            "cramps": ["Heat pad on lower abdomen", "Magnesium supplements (consult doctor)", "Gentle stretching"],
            "headache": ["Stay hydrated", "Dim lighting", "Peppermint tea", "Cold compress"],
            "fatigue": ["Iron-rich foods", "B-vitamins", "Regular sleep schedule", "Gentle movement"],
            "bloating": ["Reduce salt intake", "Herbal teas (ginger, peppermint)", "Light walks", "Stay hydrated"],
            "breast_tenderness": ["Supportive bra", "Reduce caffeine", "Evening primrose oil (consult doctor)"],
            "acne": ["Gentle skincare routine", "Stay hydrated", "Clean pillowcases", "Zinc-rich foods"]
        }
        
        # Build personalized recommendations
        recommendations = []
        
        # Add phase-based recommendations
        if phase in phase_recommendations:
            phase_rec = phase_recommendations[phase]
            recommendations.append({
                "category": "Phase-Based",
                "focus": phase_rec["focus"],
                "suggestions": phase_rec["activities"][:3],  # Top 3
                "avoid": phase_rec["avoid"]
            })
        
        # Add mood-based recommendations
        if mood in mood_recommendations:
            recommendations.append({
                "category": "Mood Support",
                "focus": f"Managing {mood} feelings",
                "suggestions": mood_recommendations[mood][:3]  # Top 3
            })
        
        # Add symptom-based recommendations
        symptom_tips = []
        for symptom in symptoms:
            if symptom in symptom_recommendations:
                symptom_tips.extend(symptom_recommendations[symptom])
        
        if symptom_tips:
            recommendations.append({
                "category": "Symptom Relief",
                "focus": "Physical symptom management",
                "suggestions": list(set(symptom_tips))[:4]  # Unique tips, max 4
            })
        
        # Supportive message
        encouragement = "Remember: You're doing great by tracking your cycle and taking care of yourself. These patterns are normal, and with awareness, you can support yourself through each phase. 💙"
        
        return {
            "status": "success",
            "cycle_phase": cycle_phase,
            "mood": mood,
            "recommendations": recommendations,
            "encouragement": encouragement,
            "note": "These are general wellness tips. For persistent concerns, please consult a healthcare provider."
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error generating recommendations: {str(e)}",
            "recommendations": []
        }

# Test the function directly 
print("✅ Recommendation generator function created")

# Test with different scenarios
test_case_1 = generate_recommendations("Luteal", "anxious", ["cramps", "fatigue"])
print(f" Test 1 (Luteal + anxious + symptoms):")
print(f"   Status: {test_case_1['status']}")
print(f"   Categories: {len(test_case_1['recommendations'])}")
if test_case_1['recommendations']:
    print(f"   Sample tip: {test_case_1['recommendations'][0]['suggestions'][0]}")

test_case_2 = generate_recommendations("Follicular", "energetic", [])
print(f" Test 2 (Follicular + energetic):")
print(f"   Status: {test_case_2['status']}")
print(f"   Focus: {test_case_2['recommendations'][0]['focus']}")

# Create the FunctionTool
recommendation_generator_tool = FunctionTool(
    func=generate_recommendations
)

print("✅ recommendation_generator_tool wrapped as FunctionTool")